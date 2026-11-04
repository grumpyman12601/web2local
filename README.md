# web2local
This is a set of instructions, commands, and scripts that allow for converting a web game to a locally stored game with all of the assets, rebuilt locally.

Why not just download the HTML?
Because most new web games reach out to a ton of different files on the server, like javascript files, 3d models, and anything else the game might need to function in the browser.

Why?
With the boom in AI recompilation, there have been a ton of full games rebuilt to run in a browser, examples are Skate 3, Terraria, Minecraft, and CSGO. The problem with this is that it's illegal to host copyrighted games this way and the projects usually get DMCA'd within the first day to first month, leaving them unplayable. This program saves all the data the game references, and rebuilds the file structure to run in a local directory on your device, so even if the site goes down, you have a saved copy.

INSTRUCTIONS FOR DOWNLOADING SITES AVAILABLE SOON
python har_download.py capture.har output_folder (Regular)

python har_download.py capture.har output_folder --host the-game-host.com (If first link isn't game hosting site)
python har_download.py capture.har output_folder --all-hosts (Do all hosts)


cd path/to/webgame
python3 -m http.server 8000
