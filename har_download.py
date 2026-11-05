#!/usr/bin/env python3
"""Usage: python har_download.py capture.har [output_folder] [--host example.com] [--all-hosts]"""
import json, os, sys, posixpath, urllib.request, urllib.parse
from collections import Counter

args = [a for a in sys.argv[1:] if not a.startswith("--")]
har_path = args[0]
out_root = args[1] if len(args) > 1 else "download"
all_hosts = "--all-hosts" in sys.argv
forced_host = None
if "--host" in sys.argv:
    forced_host = sys.argv[sys.argv.index("--host") + 1]
    if forced_host in args:
        args.remove(forced_host)
        out_root = args[1] if len(args) > 1 else "download"

with open(har_path, encoding="utf-8") as f:
    entries = json.load(f)["log"]["entries"]

# Keep HAR order (chronological), de-duplicate
seen, urls = set(), []
for e in entries:
    r = e["request"]
    u = r["url"]
    if r["method"] == "GET" and u.startswith("http") and u not in seen:
        seen.add(u)
        urls.append(u)

parsed = [urllib.parse.urlparse(u) for u in urls]

counts = Counter(p.netloc for p in parsed)
print("Hosts found in HAR:")
for h, n in counts.most_common():
    print(f"  {n:5d}  {h}")

if not all_hosts:
    host = forced_host or parsed[0].netloc
    print(f"\nUsing host: {host}  (override with --host, or use --all-hosts)\n")
    parsed = [p for p in parsed if p.netloc == host]

def rel_path(p, base):
    path = urllib.parse.unquote(p.path)
    if path.endswith("/") or not path:
        path += "index.html"
    rel = path[len(base):].lstrip("/") if base and path.startswith(base) else path.lstrip("/")
    return rel or "index.html"

ok = skipped = failed = 0
by_host = {}
for p in parsed:
    by_host.setdefault(p.netloc, []).append(p)

for host, plist in by_host.items():
    dirs = [posixpath.dirname(urllib.parse.unquote(p.path)) or "/" for p in plist]
    base = posixpath.commonpath(dirs) if dirs else "/"
    if base == "/":
        base = ""
    for p in plist:
        rel = rel_path(p, base)
        local = os.path.join(out_root, host, rel) if all_hosts else os.path.join(out_root, rel)
        if os.path.exists(local) and os.path.getsize(local) > 0:
            skipped += 1
            continue
        os.makedirs(os.path.dirname(local) or ".", exist_ok=True)
        try:
            req = urllib.request.Request(p.geturl(), headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r, open(local + ".part", "wb") as out:
                out.write(r.read())
            os.replace(local + ".part", local)
            ok += 1
            print("got ", rel)
        except Exception as e:
            failed += 1
            print("FAIL", rel, e, file=sys.stderr)
            if os.path.exists(local + ".part"):
                os.remove(local + ".part")

print(f"done: {ok} downloaded, {skipped} present, {failed} failed")