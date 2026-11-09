# web2local
This is a set of instructions, commands, and scripts that allow for converting a web game to a locally stored game with all of the assets, rebuilt locally.

### Why not just download the HTML?

Because most new web games reach out to a ton of different files on the server, like javascript files, 3d models, and anything else the game might need to function in the browser.

### Why?

With the boom in AI recompilation, there have been a ton of full games rebuilt to run in a browser, examples are Skate 3, Terraria, Minecraft, and CSGO. The problem with this is that it's illegal to host copyrighted games this way and the projects usually get DMCA'd, leaving them unplayable. This program saves all the data the game references, and rebuilds the file structure to run in a local directory on your device, so even if the site goes down, you have a saved copy.

### Isn't this illegal?

No. We don't host any copyrighted content on this repository. Keep in mind that some sites will host a copyrighted game without asking for a license or CD, this is a form of piracy and I do not condone it.

With that in mind, I'm not responsible for any misuse of this program. What you do on your own system is your own responsibility and I only support downloading legally obtainable browser games.

### Why wouldn't I just play the game through steam?

Because the web editions are significantly lighter on resources, allowing you to play them on lower-end hardware that wouldn't normally be able to run the game.

That, and most web games don't have steam pages. This means if the site goes down the internet archive is the only backup. However, the internet archive is required to comply with DMCA requests, so content can still be taken offline.


## Requirements
- Python3/Python

- WebGPU and WebGL compatible browser

- Command prompt / Shell to run scripts

## Instructions

### Downloading a game

1. Visit the game's website you'd like to save.
2. Open inspect element and navigate to the network section.
3. Clear your saved data from the site.
4. Hit Control + Shift + R to fully reload the page.
5. You'll notice that the network panel starts collecting files and assets for the game.

Depending on the way the game loads, it may load all content at once, or it may load some content at the start and then feed in data gradually as you encounter more assets.

5A. If your game just downloads all the assets at once, wait for it to finish and go to step 6 when it's done.

5B. If your game loads assets as you encounter them, navigate through all the menus, maps, and content until there isn't any more content to download. After you don't have anything else to get, go to step 6.

6. Save the output from the network pane, using the button "Export as HAR".
7. Rename the file to capture.har, and put it into a directory named after the game.
8. Make a folder called output_folder in the directory you just made.
9. Download the file har_download.py and put it into the game folder (NOT the output folder).
10. Open a command line, and run:

```bash
python har_download.py capture.har output_folder
```

10.1: If the command fails to download all content, either

- Specify the host with `--host https://your-games-host.com/` OR
- Specify to download all hosts with `--all-hosts`

11. Once the script has ran and downloaded all files into the output folder, verify there's content in the directory. Once you can verify the html page and the content around it, try to run the game.
12. To run the game locally, use the command:

```bash
python3 -m http.server 8000
```

This hosts the game and files on a local python server on port 8000, and allows you to visit `localhost:8000` in your browser and play the game.


## Additional Info

Just opening the .html page won't usually work because the browser's file viewer won't grab additional files. Exceptions are games that are hosted in a single HTML file, like Fallout NYC or New Rad City

Some games won't work out of the box, due to the structure of the files, the game trying to reach out to a server it can't access, or it could be a multitude of pathing issues.

**There's instructions for converting some games that don't work out of the box in this repo, but not every game is included and I'm adding more constantly. If you'd like to submit your own offline patch for a website, submit a pull request.**

## Commands

```bash
python har_download.py capture.har output_folder
```

```bash
python har_download.py capture.har output_folder --host the-game-host.com
```

```bash
python har_download.py capture.har output_folder --all-hosts
```

```bash
cd path/to/webgame
python3 -m http.server 8000
```
