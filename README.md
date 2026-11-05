# web2local
This is a set of instructions, commands, and scripts that allow for converting a web game to a locally stored game with all of the assets, rebuilt locally.

### Why not just download the HTML?

Because most new web games reach out to a ton of different files on the server, like javascript files, 3d models, and anything else the game might need to function in the browser.

### Why?

With the boom in AI recompilation, there have been a ton of full games rebuilt to run in a browser, examples are Skate 3, Terraria, Minecraft, and CSGO. The problem with this is that it's illegal to host copyrighted games this way and the projects usually get DMCA'd within the first day to first month, leaving them unplayable. This program saves all the data the game references, and rebuilds the file structure to run in a local directory on your device, so even if the site goes down, you have a saved copy.

### Isn't this illegal?

Not at all, it's a tool! We don't host any copyrighted content on this repo.

However, the legality of downloading certain games off of the web is iffy. Always ensure you have a legal copy of the game you're saving or are legally allowed to save it. 

I'm not responsible for any misuse of this program. What you do on your own system is your own responsibility.

### Why wouldn't I just play the game through steam?

Because the web editions are significantly lighter on resources, allowing you to play them on lower-end hardware that wouldn't normally run the game.

That, and most web games don't have steam pages so if the site goes down the internet archive is the only place to get the game. However, the internet archive is required to comply with DMCA requests, so content can still be taken offline.

## Instructions

### Downloading a game

1. Visit the game's website you'd like to save.
2. Open inspect element and navigate to the network section.
3. Clear your saved data from the site, and hit Control + Shift + R to fully reload the page
4. You'll notice that the network panel starts collecting files, like javascript files and other assets for the game

Depending on the way the game loads, it may load all content at once, or it may load some content at the start and then feed in data gradually as you encounter more assets.

5A. If your game just downloads all the assets at once, wait for it to finish and go to step 6 when it's done

5B. If your game loads assets as you encounter them, play through the game and navigate through the menus so all parts of the game get downloaded and listed in the network pane. You should have everything you need once there isn't any more content to be downloaded from the menus and game. There isn't a way to ensure you have everything, so just navigate through all menus and the game until you can't find anything else to log.

6. Save the output from the network pane, using the button "Export as HAR".
7. Rename the file to capture.har, and put it into a directory named after the game.
8. Make a folder called output_folder in the directory you just made
9. Download the file har_download.py and put it into the game folder (NOT the output folder)
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

This hosts the game files locally, and allows you to visit `localhost:8000` in your browser and play the game.

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
