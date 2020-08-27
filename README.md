[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
    <img src="images/raavaLogoNoBG.png" height="250" width="312.5">
</p>

# Table of Contents
* [Project Description](#project-description)
* [Installation](#installation)
* [Usage](#usage)

<a name="project-description"/>

# Project Description
<p>
    <img src="images/raavaOnline.jpg">
</p>

Raava is a Discord Bot Application providing extensive event logging capabilities for participating Discord Servers. Raava expands upon the logging capabilities of Discord's "Audit Log" feature to support server administrators. 

This application is written in **Python** leveraging the **Discord API** through the **discord.py** wrapper library and is hosted locally as a desktop Python application. Detailed information about this application's features and utilities can be found at <a href="https://github.com/kosamson/RaavaApp/wiki">this project's wiki</a>.

<a name="installation"/>

# Installation
#### Required Software/Tools Prior to Installation 
Python 3.7+, pip (if not already installed), Discord account

#### Required Python Packages (install using pip) 
dotenv, discord, pytz 

#### Section 1: Creating and Configuring Your RaavaApp Application
Raava is not currently hosted online, so you must create and configure a Discord Application to host your Bot locally and connect with the code provided in this repository.

1. Clone this repository to an accessible location.
2. Create a Discord Application to host your Raava Bot on the Discord Developers Portal (click on `New Application` located at: https://discord.com/developers/applications).
3. Click on the `Bot` tab and obtain your personal Bot Token by clicking `Copy` under the Token subsection.
    **NOTE: Do NOT post this Token anywhere or reveal it to anyone else, this Token can allow others to take control and make malicious changes to your Bot.**
4. Open your locally cloned RaavaApp folder and go to the `src` folder.
5. Open `example.env` in a text editor (Notepad, Notepad++, VS Code, etc.) and replace `INSERT_TOKEN_HERE` with your copied Bot Token.
6. Rename `example.env` to `.env`.

#### Section 2: Adding Raava to Your Server
Your RaavaApp application has now been setup, and now you must add Raava to your Discord server.

1. Go back to your RaavaApp page on the Discord Developers Portal.
2. Click to the `OAuth2` tab.
3. Check the *bot* checkbox under the **Scopes** subsection.
4. Check the *Administrator* checkbox under the **Bot Permissions** subsection (which should have appeared after you checked the previous checkbox).
5. Click the `Copy` button next to the URL generated under the **Scopes** subsection and paste it into your browser's navigation bar.  
6. Press Enter, and on the proceeding webpage, select the server you wish to add Raava to.
7. Click `Authorize` 

#### Section 3: Starting Raava
Raava has now been successfully added to your server, and now you just need to start the Bot! For the final steps, see the <a href="#usage">**Usage**</a> section.

<a name="usage"/>

# Usage
Raava's Bot capabilities can be started using the command line.

#### Steps
1. Open up your operating system's command line utility/terminal (Windows: Command Prompt, Mac & Linux: Terminal)
2. Navigate to your local cloned directory of this RaavaApp repository
3. Navigate to the `src` directory
4. Enter into console: 
```
python init.py
```

Raava will now be connected to the Discord client and online in your server. Upon successful launch, your terminal will display a startup message that looks like this (except with your unique name for Raava and server you connected it to): 
```
Raava#1234 is now connected.\nConnected to Guilds:\n\tGuild Name: Example Guild, Guild ID: 123456789987654321
```

Now you can perform any of Raava's utilities on your server. If you want to shut down Raava from your server, use the `+shutdown` command. A successful shutdown will print this into your terminal window:
```
Bot shutting down by command from Guild: Example Guild (Guild ID: 123456789987654321) by user: someguy#4321
```

Then, if you want to restart Raava, simply repeat the steps listed in this section.

