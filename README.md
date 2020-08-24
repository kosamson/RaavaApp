<p align="center">
    <img src="images/raavaLogo.jpg" height="200" width="250">
</p>

# Table of Contents
* [Raava](#raava)
* [Commands](#commands)
* [Logging](#logging)

<a name="raava"/>

# Raava
Raava is a Discord Bot Application that provides basic server information, server logging, and various other fun text-based commands that users can invoke in their personal Discord Servers.

<a name="commands"/>

# Commands
The command prefix for Raava's commands is '+'. For example, in order to execute the help command, you would type: `+help` in a Discord text channel that has Raava added to their server.

* **cring** - Sends a message containing the phrase "CRING" to the text channel where this command was invoked.

* **cringreact** - Adds the reaction: `C R I N G` (using Discord's regional indicator letter emojis) to the message prior to the message invoking this command. Deletes the message that invokes this command after adding reactions. 

* **help** - Default help command for information about Raava and its associated commands. Sends a direct message (DM) to the command invoker containing a link to this README document and a list of Raava's commands.

* **getavatar \[USER_ID\]** - Retrieves and sends the respective server member's icon image. Input parameter is the respective server member's Discord ID (can be retrieved by right-clicking on the user and clicking "Copy ID") .

* **postcring** - Sends a random "YOU POSTED CRING" image to the text channel where this command is invoked.

* **servericon** - Retrieves and sends the respective server's icon image where this command is invoked.

* **shutdown** - Disconnects Raava Bot's Discord Client connection and shuts the bot down. *Only available to members who have the `Administrator` role permission in the respective server(s) which Raava is connected to*.

<a name="logging"/>

# Logging
Raava enables for file-based logging of different user/server events in your local directory of `RaavaApp`. Logs for all servers which Raava is added to can be found by default in the RaavaApp directory: `RaavaApp\serverlogs\`. 

Logs for each specific server that Raava is connected to are located in a folder labeled by the server's unique ID. For example, the Discord server that has the ID `123456789` will have their respective log files stored in the directory: `RaavaApp\serverlogs\123456789`.

#### \@everyone/\@here Logging
Whenever a user invokes a mass-ping on the server through the `@everyone` or `@here` commands, Raava will log their Discord username, user discriminator, and a timestamp of when their message containing the mass-ping was sent in the file: `evLog.txt`. 

#### Member Removal Logging
Whenever a user is kicked, banned, leaves, or is removed in some other fashion, Raava will log their Discord username, user discriminator, and a timestamp of when they were removed in the file `leaveLog.txt`.
