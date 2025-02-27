from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from enum import Enum
import time
import json
import os

# shower state class to account for broken
class ShowerState(Enum):
    ON = "on"
    OFF = "off"
    BROKEN = "broken"

# default config values
default_config = {
  "life_support_on": True,
  "keycard_supplied": False,
  "keycard_pin": "2122",  # Alien takes place this year ;)
  "showers": {
    1: ShowerState.OFF,
    2: ShowerState.OFF,
    3: ShowerState.OFF,
    4: ShowerState.OFF,
    5: ShowerState.BROKEN  
  },
  "dock_1_locked": True,
  "dock_1_ship": "Heracles",
  "dock_2_locked": False,
  "dock_2_ship": "Grasshopper",
  "mineshaft_locked": False
}



# non menu functions here

# shower toggle
def shower_toggle(num):
  global config
  if config["showers"][num] == ShowerState.ON:
    print(f"TURNING OFF SHOWER {num}")
    config["showers"][num] = ShowerState.OFF
    time.sleep(2)
  elif config["showers"][num] == ShowerState.OFF:
    print(f"TURNING SHOWER {num} ON")
    config["showers"][num] = ShowerState.ON
    time.sleep(2)
  elif config["showers"][num] == ShowerState.BROKEN:
    time.sleep(1)
    print(...)
    time.sleep(12)
    print("ERROR: NOTIFICATION LEVEL")
    print(f"SHOWER {num} NOT RESPONDING")
    time.sleep(1)
        

# json saving
def save_config_to_file(config, filename):
  with open(filename, "w") as file:
    json.dump(config, file, indent=4)

# usage:
# save_config_to_file(config, "config.json")

# json loading

def load_config_from_file(filename, default_config):
  if os.path.exists(filename):
    with open(filename, "r") as file:
      config = json.load(file)
      # Convert shower states back to enum
      for key, value in config["showers"].items():
          config["showers"][key] = ShowerState(value)
      return config
  else:
    return default_config

# load config if it exists, otherwise use default values supplied above.
config = load_config_from_file("config.json", default_config)


# Menu functions start here
def bootup():
  print (r"""__   __        _ _               _____ _        _   _             
\ \ / /       (_) |             /  ___| |      | | (_)            
 \ V / __  ___ _| | ___  _ __   \ `--.| |_ __ _| |_ _  ___  _ __  
  \ / '_ \/ __| | |/ _ \| '_ \   `--. \ __/ _` | __| |/ _ \| '_ \ 
  | | |_) \__ \ | | (_) | | | | /\__/ / || (_| | |_| | (_) | | | |
  \_/ .__/|___/_|_|\___/|_| |_| \____/ \__\__,_|\__|_|\___/|_| |_|
    | |                                                           
    |_|              
FLEET COMMODORE SYSTEMS © 2246 - GUILD LICENSE
PROGRAM OPERATION GROUP SOFTWARE (P.O.G.S.)
----------
WARNING - LICENSE EXPIRED
CONTACT SYSTEMS ADMINISTRATOR
----------
""")
  main_menu()
    
def main_menu():
  print ("YPSILON 14 CONTROL TERMINAL")
  time.sleep(1)
  print ("""> DIAGNOSTICS
> SCHEDULE
> CONTROLS
> ROSTER
> COMMS
""")
  menu_completer = WordCompleter(['DIAGNOSTICS', 'SCHEDULE', 'CONTROLS', 'ROSTER', 'COMMS'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      quit()
    elif choice.lower() == 'diagnostics':
      option_diagnostics()
    elif choice.lower() == 'schedule':
      option_schedule()
    elif choice.lower() == 'controls':
      option_controls()
    elif choice.lower() == 'roster':
      option_roster()
    elif choice.lower() == 'comms':
      menu2()
    elif choice.lower() == 'throw rock':
      print ("\nYou decided to throw another rock, as if the first " 
      "rock thrown did much damage. The rock flew well over the "
      "orcs head. You missed. \n\nYou died!")
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      main_menu()

def option_diagnostics(): 
  print ("\nDIAGNOSTICS")
  time.sleep(1)
  print ("""> LAYOUT
> STATUS
< BACK""")
  menu_completer = WordCompleter(['LAYOUT', 'STATUS', 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      break
    elif choice.lower() == 'layout':
      option_layout()
    elif choice.lower() == 'status':
      option_status()
    elif choice.lower() == 'back':
      main_menu()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_diagnostics()

def option_layout():
  print ("\nGENERATING LAYOUT")
  time.sleep(1)
  print (r"""▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓__   _____  ___ ___ _    ___  _  _   _ _ _  ▓
▓\ \ / / _ \/ __|_ _| |  / _ \| \| | / | | | ▓
▓ \ V /|  _/\__ \| || |_| (_) | .` | | |_  _|▓
▓  |_| |_|  |___/___|____\___/|_|\_| |_| |_| ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓ | DOCK 1| DOCK 2|         ▓▓GUILD LICENSE▓▓▓
▓    ] [     ] [            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓  ___X_______X___     ______    _________   ▓
▓ |      =C=      |   |8 |9|0|  | ooo /\  |  ▓
▓ |   WORKSPACE   |___|7     |__| MESS    |  ▓
▓ |               ____     _____  ooo  0  |  ▓
▓ |    \----/     |   |_    1|  |_________|  ▓
▓ |    /MINE\     |   |6   |_|__|  WASH ~~|  ▓
▓ |    \----/     |   |5    ____   ROOM ~~|  ▓
▓ |_______________|   |4|3|2 |  |_|_|_|_|_|  ▓
▓        o↑           QUARTERS               ▓
▓       _o↓_          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓      X___|MINESHAFT ▓        ROSTER        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 1 SONYA    6 MORGAN  ▓
▓-------LEGEND--------▓ 2 ASHRAF   7 RIE     ▓
▓  X    AIRLOCK       ▓ 3 DANA     8 ROSA    ▓
▓ =C=  COMPUTER       ▓ 4 JEROME   9 MIKE    ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 5 KANTARO  0 N/A     ▓
▓  DOCK 1  ▓  DOCK 2  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓ HERACLES ▓ RESUPPLY ▓VERSION SOFTWARE 2.25B▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""")
  choice = input("<PRESS RETURN>")
  if choice:
   option_diagnostics()

def option_status():
  print ("\nSTATUS")
  time.sleep(1)
  print ("SYSTEMS CHECK ...")
  time.sleep(3)
  print (""" WARNING: AIR FILTERS LAST REPLACED 455 DAYS AGO
(255 DAYS PAST RECOMMENDATION)
WARNING: SHOWER 5 OUT OF ORDER AS OF 1 DAY AGO
WARNING: MINESHAFT ELEVATOR LAST MAINTAINED 455 DAYS AGO
(255 DAYS PAST RECOMMENDATION)
WARNING: AIRFLOW 82%
(SUBOPTIMAL: REPLACE FILTERS AND CHECK VENTS FOR BLOCKAGES)
ALL SYSTEMS WITHIN ACCEPTABLE OPERATING CONDITIONS
""")
  choice = input("<PRESS RETURN>")
  if choice:
    option_diagnostics()

def option_schedule():
  print ("\nSCHEDULE")
  time.sleep(1)
  print ("""2255-07-02 06:33 - IMV GRASSHOPPER    - RESUPPLY - DOCKING BAY 2 - DOCK
2255-06-04 08:34 - RSV THE HERACLES   - RESEARCH - DOCKING BAY 1 - DOCK
2255-06-02 12:23 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-06-01 16:04 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-05-02 08:32 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-05-01 06:02 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
2255-04-02 13:02 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-04-01 15:54 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-03-02 08:33 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-03-01 06:04 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
""")
  choice = input("<PRESS RETURN>")
  if choice:
    main_menu()

def option_roster():
  print ("\nROSTER")
  time.sleep(1)
  print ("""01. VERHOEVEN, SONYA     - OVERSEER
02. SINGH, ASHRAF        - BREAKER
03. DE BEERS, DANA       - HEAD DRILLER
04. HUIZINGA, JEROME     - ASST. DRILLER
05. TOBIN, ROSA          - MINING ENGINEER
06. MIKKELSEN, MICHAEL   - MINING ENGINEER
07. KANTARO, KENJI       - LOADER
08. OBOWE, MORGAN        - LOADER
09. KENBISHI, RIE        - PUTTER
10. VACANT
""")
  choice = input("<PRESS RETURN>")
  if choice:
    main_menu()

def option_controls(): 
  print ("\nCONTROLS")
  time.sleep(1)
  print ("""> AIRLOCKS
> SHOWERS
> SYSTEM [A]
< BACK""")
  menu_completer = WordCompleter(['AIRLOCKS', 'SHOWERS', 'SYSTEM [ADMIN]', 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      break
    elif choice.lower() == 'airlocks':
      option_airlocks()
    elif choice.lower() == 'showers':
      option_showers()
    elif choice.lower() == 'system':
      option_system()
    elif choice.lower() == 'back':
      main_menu()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_controls()

def option_airlocks():
  global config
  print ("\nTOGGLE WHICH AIRLOCK?")
  time.sleep(1)
  if config["dock_1_locked"] == True:
    print ("DOCKING BAY 1 [> LOCKED]")
  else:
    print ("DOCKING BAY 1 [> UNLOCKED]")
  if config["dock_2_locked"] == True:
    print ("DOCKING BAY 2 [> LOCKED]")
  else:
    print ("DOCKING BAY 2 [> UNLOCKED]")
  if config["mineshaft_locked"] == True:
    print ("MINESHAFT [> LOCKED]")
  else:
    print ("MINESHAFT [> UNLOCKED]")
  print ("< BACK")
  menu_completer = WordCompleter(['DOCKING BAY 1', 'DOCKING BAY 2', 'MINESHAFT', 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      break
    if choice.lower() == 'docking bay 1':
      if config["dock_1_locked"] == False:
        print ("INITIALIZING BAY 1 LOCK.\nNOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
        time.sleep(3)
        print ("\nDOCKING BAY 1 LOCKED")
        time.sleep(1)
        config["dock_1_locked"] = True
        option_airlocks()
      else:
        print ("UNLOCKING BAY 1")
        time.sleep(3)
        print ("\nDOCKING BAY 1 UNLOCKED")
        time.sleep(1)
        config["dock_1_locked"] = False
        option_airlocks()
    if choice.lower() == 'docking bay 2':
      if config["dock_2_locked"] == False:
        print ("INITIALIZING BAY 2 LOCK.\nNOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
        time.sleep(3)
        print ("\nDOCKING BAY 2 LOCKED")
        time.sleep(1)
        config["dock_2_locked"] = True
        option_airlocks()
      else:
        print ("UNLOCKING BAY 2 AIRLOCK")
        time.sleep(3)
        print ("\nDOCKING BAY 2 UNLOCKED")
        time.sleep(1)
        config["dock_2_locked"] = False
        option_airlocks()
    if choice.lower() == 'mineshaft':
      if config["mineshaft_locked"] == False:
        print ("INITIALIZING MINESHAFT LOCK.\nNOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
        time.sleep(3)
        print ("\nMINESHAFT AIRLOCK LOCKED")
        time.sleep(1)
        config["mineshaft_locked"] = True
        option_airlocks()
      else:
        print ("UNLOCKING MINESHAFT AIRLOCK")
        time.sleep(3)
        print ("MINESHAFT AIRLOCK UNLOCKED")
        time.sleep(1)
        config["mineshaft_locked"] = False
        option_airlocks()
    elif choice.lower() == 'back':
      option_controls()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_airlocks()

def option_showers():
  global config
  print ("\nTOGGLE WHICH SHOWER NUMBER?")
  for shower_id, state in config["showers"].items():
    if state == ShowerState.ON:
      print(f"SHOWER {shower_id} [> ON ]")
    elif state == ShowerState.OFF:
      print(f"SHOWER {shower_id} [> OFF]")
    elif state == ShowerState.BROKEN:
      print(f"SHOWER {shower_id} [ERROR]")
  print ("< BACK")
  menu_completer = WordCompleter(['BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      main_menu()
    if choice in ["1","2","3","4","5"]:
      shower_toggle(int(choice))
      option_showers()
    elif choice.lower() == 'back':
      option_controls()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_showers()

def option_system():
  global config
  if config["keycard_supplied"] == True:
   option_system_a()
  else:
   print ("SYSTEM")
  time.sleep(1)
  print("PLEASE INSERT ADMINISTRATOR KEYCARD\n")
  print("READY TO READ KEYCARD?")
  choice = input("[Y/N]")
  if choice.lower() == "y":
    time.sleep(1)
    print("ACCESSING KEYCARD SLOT\n")
    time.sleep(1)
    pin_input = input("KEYCARD PIN ID [XXXX]:")
    if pin_input == config["keycard_pin"]:
    config["keycard_supplied"] = True
    option_system_a()
  elif choice.lower() == "n":
    option_controls()
  else:
    print ("PLEASE INDICATE YES OR NO")
    time.sleep(1)
    option_system()

if __name__ == '__main__':
  bootup()