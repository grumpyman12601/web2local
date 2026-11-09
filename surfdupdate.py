from pathlib import Path

path = Path(r"C:\Users\user\Downloads\path\to\surfd\output_folder\surfd.net\assets\game-CrU_KUAb.js")
text = path.read_text(encoding="utf-8", errors="ignore")

marker = '};if(Q?.session===P&&Q.commands===P.commands){'
replacement = '};Q={session:P,commands:P.commands};if(Q?.session===P&&Q.commands===P.commands){'

count = text.count(marker)
if count != 1:
    raise SystemExit(f"Expected exactly one matching insertion point; found {count}. File unchanged.")

backup = path.with_suffix(path.suffix + ".bak")
backup.write_text(text, encoding="utf-8")
path.write_text(text.replace(marker, replacement, 1), encoding="utf-8")

print(f"Patched {path}")
print(f"Backup saved as {backup}")
