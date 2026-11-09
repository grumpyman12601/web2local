**Surfd.net CSGO Slide Offline Patch Instructions**

Open the surfdupdate.py file, and edit the directory in the script to match the path to the game file game-CrU_KUAb.js, located in:

```C:\Users\user\Downloads\path\to\surfd\output_folder\surfd.net\assets\game-CrU_KUAb.```

Run the python script ```surfdupdate.py``` with the command ```python surfdupdate.py```
The script makes the game always select local-only play, so you don't have to select it every time you respawn

Replace this fragment in 
```C:\Users\user\Downloads\path\to\surfd\output_folder\surfd.net\assets\game-CrU_KUAb.js```

```if(p){t.invalidate(),i.invalidate(),Ce("blocked","Online saving is unavailable. Press Esc to retry or choose local play. "+p);return}if(!e.config.enabled```

with this:

```if(p){Q={session:P,commands:P.commands};t.invalidate(),i.invalidate(),Ce("local","Local-only run selected.");return}if(!e.config.enabled```

**Just replace that snippet in the file, don't overwrite the whole line.**

Save the file, and then launch a local server to test.
