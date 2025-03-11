# ypsilonconsole
A python-coded ypsilon 14 console, based on the Mothership module and Quadra's traaash version

Forked from tempest-creator.

evilkorova fork info:
- rebuilt and restructured using prompt_toolkit, json, and enum libraries.
- it will now autocomplete commands, which helps user know what to type (still has hidden commands)
- airlock and shower controls are now a toggle to reduce the amount of commands necessary
- ships are now variables to easily change their names
- showers can now be broken (5 defaults to broken)
- upon exit it will save the configurations to a json file. 
- upon boot again it will use the json file instead of the default config keys.
- there is now a hacker shell (hidden menu) that GM (or a hacker player) can use to change ship names, fix showers, and backdoor into admin settings. (see below)
- keycard control is now 2 factor (see below)

This is my version I made for my game, so there are some changes and departures that are preference only.

Links:
Based on: https://www.traaa.sh/the-ypsilon-14-terminal

Original: https://github.com/tempest-creator/ypsilonconsole

Cool Retro Term to complete the look:  https://github.com/Swordfish90/cool-retro-term

# Instructions

1. Install python3 (if you don't have it)
1. install prompt_toolkit library (pip3 install prompt_toolkit)
1. edit the config dictionary in terminal.py for any defaults you want to change
1. launch terminal.py (python3 terminal.py), preferably using cool-retro-term!

# Sonya's keycard
Access control for Sonya's keycard now has a second factor ("What you know") in addition to the keycard ("What you have"). The default is 2122 (the year Alien takes place.)  I would place it in an easily found location, possibly even written on the keycard or taped to the terminal itself. This is mainly just to make the program validate that the players did indeed find a keycard instead of just typing "insert keycard" or something. 

# Hacker shell
Player 1: I'd like to try to hack the terminal.

Warden: Okay, roll an Intellect check please, at disadvantage since you are not a skilled hacker. 

Player 2: Oh I have the hacking expert skill, can I try instead? 

Warden: Absolutely, roll Intellect with the hacking bonus. 

Player 2: I got a 34, my Intellect is 31 not counting my hacking skill.

Warden: You are familiar with terminal models like this one. There is a service access panel in the back that service engineers open and insert their service key. 

Player 2: Okay I take off the panel.

Warden: Flipping that open you notice that on the exposed PCB there are a couple of pins you can probably jump together in order to bypass the service key. Once that is done it will only be a matter of accessing the service menu by typing "run init 1337" at the main menu.

## The shell
You can access the shell with "run init 1337" at the main/top level only.

The shell has no levels and you can tab through the commands so the user doesn't have to memorize what options are available. You can also use "?" to see all commands. This is a useful menu for changing ship names, setting shower 5 to not be broken (both commands the warden could do when nobody is looking), but the main use is to provide them a way to access the keycard only sections by using the keycard override.

REGISTER BAY 1 SHIP

REGISTER BAY 2 SHIP

HYDROCONTROLLER SELFREPAIR

HYDROCONTROLLER STATUS

HYDROCONTROLLER SHUTOFF

KEYCARD OVERRIDE

