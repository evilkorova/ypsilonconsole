# ypsilonconsole
A python-coded ypsilon 14 console, based on the Mothership module and Quadra's traaash version

Forked from tempest-creator.

evilkorova fork info (work in progress):
- rebuilt and restructured using prompt_toolkit library
- it will now autocomplete which helps user know what to type (still has hidden commands)
- airlock controls are now a toggle to reduce the amount of commands necessary
- ships are now variables to easily change their names

would be cool (maybe one day, probably won't)
- drop the global variable keys to a json file so states are saved between runs and....  
- add a menu option to edit ("register") ship names.

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
