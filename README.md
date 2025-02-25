# ypsilonconsole
A python-coded ypsilon 14 console, based on the Mothership module and Quadra's traaash version

Forked from tempest-creator.

evilkorova fork info (work in progress):
- rebuilt and restructured using prompt_toolkit, json, and enum libraries.
- it will now autocomplete commands, which helps user know what to type (still has hidden commands)
- airlock and shower controls are now a toggle to reduce the amount of commands necessary
- ships are now variables to easily change their names
- showers can now be broken (5 defaults to broken)
- upon exit it will save the configurations to a json file. 
- upon boot again it will use the json file instead of the default config keys.
- there is now a hacker shell (hidden menu) that GM (or a hacker player) can use to change ship names, break showers, and backdoor into admin settings. (see below)
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
Access control for Sonya's keycard now has a second factor ("What you know") in addition to the keycard ("What you have"). The default is 2122 (the year Alien takes place.)  I would have it in an easily found location, possibly even written on the keycard or taped to the terminal itself. This is mainly just to make the program validate that the players did indeed find a keycard instead of just typing "insert keycard" or something. 

# Hacker shell
The hacker shell can be accessed only from the main (top) menu. I have it as a config key so you can set it to whatever you want but the default is "run init 1337". I know it's probably too corny to be running 1337 jokes but maybe your players are old like mine. Again this is easily changeable in the configuration settings.

The shell has no levels and you can tab through the commands so the user doesn't have to memorize what options are available.

REGISTER BAY 1 SHIP

REGISTER BAY 2 SHIP

CONTROLLER SHOWER OVERCLOCK

CONTROLLER SHOWER REPAIR

SYSTEM LIFE SUPPORT ON/OFF

SYSTEM SELF-DESTRUCT

