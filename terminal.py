from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from enum import Enum
import time
import json
import os
import random

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
  "dock_1_ship": "HERACLES",
  "dock_2_locked": False,
  "dock_2_ship": "IMV GRASSHOPPER",
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
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("ERROR: NOTIFICATION LEVEL")
    print(f"SHOWER {num} NOT RESPONDING")
    while True:
      ret_choice = input("<RETURN>")
      if ret_choice == "":
        time.sleep(1)

        

# json saving
def custom_serializer(obj):
    if isinstance(obj, ShowerState):
        return obj.name  # Save the enum as its name (e.g., "OFF", "BROKEN")
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def save_config_to_file(config, filename):
    with open(filename, "w") as file:
        json.dump(config, file, indent=2, default=custom_serializer)

# usage:
# save_config_to_file(config, "config.json")

# json loading
def load_config_from_file(filename, default_config):
  if os.path.exists(filename):
    with open(filename, "r") as file:
      config = json.load(file)
      # Convert shower states back to enum
      config["showers"] = {
        int(key): ShowerState[value]  # Convert string key to int, and value back to enum
        for key, value in config["showers"].items()
      }
      return config
  else:
    return default_config

# def paginate_output(text_blob, page_size=10):
#   lines = text_blob.splitlines()
#   for i in range(0, len(lines), page_size):
#     print("\n".join(lines[i:i+page_size]))
#     input("\n[RETURN]")

# load config if it exists, otherwise use default values supplied above.
config = load_config_from_file("config.json", default_config)

# Menu functions start here
def bootup():
  time.sleep(1)
  print (r"""__   __        _ _               _____ _        _   _             
\ \ / /       (_) |             /  ___| |      | | (_)            
 \ V / __  ___ _| | ___  _ __   \ `--.| |_ __ _| |_ _  ___  _ __  
  \ / '_ \/ __| | |/ _ \| '_ \   `--. \ __/ _` | __| |/ _ \| '_ \ 
  | | |_) \__ \ | | (_) | | | | /\__/ / || (_| | |_| | (_) | | | |
  \_/ .__/|___/_|_|\___/|_| |_| \____/ \__\__,_|\__|_|\___/|_| |_|
    | |                                                           
    |_|        
""")
  time.sleep(2)
  print (r"""      
FLEET COMMODORE SYSTEMS © 2246 - GUILD LICENSE
PROGRAM OPERATION GROUP SOFTWARE (P.O.G.S.)
----------
WARNING - LICENSE EXPIRED
CONTACT SYSTEMS ADMINISTRATOR
----------
BOOTING...
""")
  time.sleep(3)
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
      save_config_to_file(config, "config.json")
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
      option_comms()
    elif choice.lower() == 'throw rock':
      print ("\nYou decided to throw another rock, as if the first " 
      "rock thrown did much damage. The rock flew well over the "
      "orcs head. You missed. \n\nYou died!")
    elif choice.lower() == 'run init 1337':
      print("INITIALIZING SERVICE UPDATE")
      time.sleep(1)
      hacker_shell()
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
  layout = r"""▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
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
"""
# can uncomment the below to paginate layout (and def above)
#  paginate_output(layout)
  print(layout)
  while True:
    ret_choice = input("<RETURN>")
    if ret_choice == "":
      time.sleep(1)
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
  while True:
    ret_choice = input("<RETURN>")
    if ret_choice == "":
      time.sleep(1)
      option_diagnostics()

def option_schedule():
  global config
  ship_1_name = config["dock_1_ship"]
  ship_2_name = config["dock_2_ship"]
  print ("\nSCHEDULE")
  time.sleep(1)
  print (f"""2255-07-02 06:33 - {ship_1_name}    - RESUPPLY - DOCKING BAY 2 - DOCK
2255-06-04 08:34 - {ship_2_name}    - RESEARCH - DOCKING BAY 1 - DOCK
2255-06-02 12:23 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-06-01 16:04 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-05-02 08:32 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-05-01 06:02 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
2255-04-02 13:02 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-04-01 15:54 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-03-02 08:33 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-03-01 06:04 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
""")
  while True:
    ret_choice = input("<RETURN>")
    if ret_choice == "":
      time.sleep(1)
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
  while True:
    ret_choice = input("<RETURN>")
    if ret_choice == "":
      time.sleep(1)
      main_menu()

def option_controls(): 
  print ("\nCONTROLS")
  time.sleep(1)
  print ("""> AIRLOCKS
> SHOWERS
> SYSTEM [ADMIN]
< BACK""")
  menu_completer = WordCompleter(['AIRLOCKS', 'SHOWERS', 'SYSTEM', 'BACK'], ignore_case=True)
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
  time.sleep(1)
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
   time.sleep(1)
   print("[ACCESS GRANTED]")
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
      time.sleep(1)
      print ("[ACCESS GRANTED. WELCOME, SONYA.]")
      time.sleep(2)
      option_system_a()
    else:
      print("AUTHORIZATION DENIED")
      time.sleep(3)
      option_controls()
  elif choice.lower() == "n":
    option_controls()
  else:
    print ("PLEASE INDICATE YES OR NO")
    time.sleep(1)
    option_system()

def option_system_a():
  print ("""SYSTEM
> LIFE SUPPORT
> SCUTTLE
< BACK""")
  menu_completer = WordCompleter(['LIFE SUPPORT', 'SCUTTLE', 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'life support':
      option_lifesupport()
    elif choice.lower() == 'scuttle':
      option_scuttle()
    elif choice.lower() == 'back':
      option_controls()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_system_a()

def option_lifesupport():
  global config
  time.sleep(1)
  if config["life_support_on"] == True:
    print ("LIFE SUPPORT [> ON]")
    print("\nWARNING:\nENSURE ALL PERSONNEL ARE IN VACCSUITS BEFORE TURNING OFF LIFE SUPPORT")
    print("\nTURN LIFE SUPPORT OFF?")
    choice = input("[Y/N]")
    if choice.lower() == "y":
      config["life_support_on"] = False
      time.sleep(1)
      print("DISABLING LIFE SUPPORT\n")
      time.sleep(1)
      print("WARNING: LIFE SUPPORT DISABLED")
      while True:
        ret_choice = input("<RETURN>")
        if ret_choice == "":
          time.sleep(1)
          option_system_a()
    elif choice.lower() == "n":
      time.sleep(1)
      option_system_a()
    else:
      print ("PLEASE INDICATE YES OR NO")
      time.sleep(1)
      option_lifesupport()
  else:
    print ("LIFE SUPPORT [> OFF]")
    print("\nTURN LIFE SUPPORT ON?")
    choice = input("[Y/N]")
    if choice.lower() == "y":
      config["life_support_on"] = True
      time.sleep(1)
      print("ENABLING LIFE SUPPORT\n")
      time.sleep(1)
      print("LIFE SUPPORT ENABLED")
      print("WARNING: ENSURE ALL PERSONNEL REMAIN IN VACCSUITS FOR 5 MINUTES\n")
      while True:
        ret_choice = input("<RETURN>")
        if ret_choice == "":
          time.sleep(1)
          option_system_a()
    elif choice.lower() == "n":
      time.sleep(1)
      option_system_a()
    else:
      print ("PLEASE INDICATE YES OR NO")
      time.sleep(1)
      option_lifesupport()

def option_scuttle():
  print ("SCUTTLE")
  time.sleep(1)
  print("[WARNING] THIS WILL INITIATE A 10-MINUTE STATION SELF-DESTRUCT SEQUENCE")
  print("\nINITIATE SELF DESTRUCT")
  choice = input("[Y/N]")
  if choice.lower() == "y":
    time.sleep(1)
    print("[WARNING] SEQUENCE IS IRREVERSIBLE AFTER 5 MINUTES\n")
    time.sleep(1)
    choice = input("CONTINUE? [Y/N]")
    if choice.lower() == "y":
      time.sleep(1)
      print('TYPE "SCUTTLE" TO CONFIRM:')
      choice = input(" >>>")
      if choice.lower() == "scuttle":
        time.sleep(2)
        print ("STATION WILL SELF-DESTRUCT IN 10 MINUTES.\n")
        time.sleep(2)
        print ("IMMEDIATE EVACUATION SUGGESTED.\n")
        start_time = time.time()
        abort_choice = None
        while time.time() - start_time < 300:
          print('TYPE "ABORT" TO CANCEL')
          abort_choice = input(" >>>")
          if abort_choice.lower() == "abort":
            break
        if abort_choice.lower() == "abort":
            print("ABORTING")
            time.sleep(2)
            option_system_a()
        print("[WARNING] SELF-DESCTRUCT IN 5 MINUTES\n")
        time.sleep(1)
        print("[WARNING] SEQUENCE IS NO LONGER REVERSIBLE\n")
        time.sleep(4)
        print("HAVE A NICE DAY :)")
        time.sleep(295)
        print("(boom)")
        while True:
          pass
      else:
        print("CANCELING SELF DESTRUCT\n")
        time.sleep(3)
        option_system_a()
  elif choice.lower() == "n":
    print("ABORTING")
    time.sleep(2)
    option_system_a()
  else:
    print ("PLEASE INDICATE YES OR NO")
    time.sleep(1)
    option_scuttle()

def option_comms():
  global config
  ship_1_name = config["dock_1_ship"]
  ship_2_name = config["dock_2_ship"]
  print("COMMS")
  time.sleep(1)
  print("SCANNING FOR NEARBY SHIPS...\n")
  time.sleep(3)
  print("SHIPS IN RANGE BELOW. TYPE NAME TO HAIL\n")
  print(ship_1_name)
  print(ship_2_name)
  print("\n< BACK")
  menu_completer = WordCompleter([ship_1_name, ship_2_name, 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == ship_2_name.lower():
      print(f"HAILING {ship_2_name}")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      print("COMMUNICATION CHANNEL OPEN")
      print("PRESS RETURN TO END CALL")
      while True:
        ret_choice = input("[RETURN]")
        if ret_choice == "":
          time.sleep(1)
          main_menu()
    elif choice.lower() == ship_1_name.lower():
      print(f"HAILING {ship_1_name}")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(2)
      print("NO ANSWER")
      while True:
        ret_choice = input("<RETURN>")
        if ret_choice == "":
          time.sleep(1)
          main_menu()
    elif choice.lower() == 'back':
      main_menu()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_comms()

def hacker_shell():
  global config
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("ERROR")
  time.sleep(2)
  print("Ǝ⊥∀ᗡԀ∩ ƎƆIΛᴚƎS ⅁NIZI˥∀I⊥INI\n")
  time.sleep(2)
  print("ERROR\n")
  time.sleep(2)
  print("ᴚOᴚᴚƎ\n")
  time.sleep(2)
  print("乇尺尺ㄖ尺\n")
  time.sleep(2)
  print("INTERRUPTING\n")
  time.sleep(2)
  print("ł₦₮ɆⱤⱤɄ₱₮ł₦₲\n\n")
  time.sleep(3)
  print("WELCOME TO THE SERVICE EN₲ł₦ɆE̶R̶ INTERFACE\nAUTHORłⱫɆĐ PERSONNEL ONLY")
  character_pool = (
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Uppercase ASCII letters
  "abcdefghijklmnopqrstuvwxyz"  # Lowercase ASCII letters
  "0123456789"                  # Digits
 # "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
 # "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
  "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
  "αβγδεζηθικλμνξοπρστυφχψω"
  )
  menu_completer = WordCompleter(['REBOOT', 'REGISTER BAY 1 SHIP', 'REGISTER BAY 2 SHIP', 'HYDROCONTROLLER SELFREPAIR', 'HYDROCONTROLLER STATUS', 'HYDROCONTROLLER OVERRIDE', 'KEYCARD OVERRIDE'], ignore_case=True)
  while True:
    random_characters = ''.join(random.choices(character_pool, k=5))
    choice = prompt(f'{random_characters}> ', completer=menu_completer)
    if choice == "?":
      print("AVAILABLE COMMANDS")
      time.sleep(1)
      print("""      
REGISTER BAY 1 SHIP
REGISTER BAY 2 SHIP
HYDROCONTROLLER SELFREPAIR
HYDROCONTROLLER STATUS
HYDROCONTROLLER OVERRIDE
KEYCARD OVERRIDE
REBOOT""")
    elif choice.lower() == "reboot":
      bootup()
    elif choice.lower() == "register bay 1 ship":
      print("\nREGISTER NEW NAME FOR SHIP IN BAY 1")
      while True:
        bay_1_name = prompt(">>> ")
        if bay_1_name:
          config["dock_1_ship"] = bay_1_name.upper()
          print(f"\nREGISTERED NEW NAME: {bay_1_name.upper()}")
          break
        else:
          break
    elif choice.lower() == "register bay 2 ship":
      print("\nREGISTER NEW NAME FOR SHIP IN BAY 2")
      while True:
        bay_2_name = prompt(">>> ")
        if bay_2_name:
          config["dock_2_ship"] = bay_2_name.upper()
          print(f"\nREGISTERED NEW NAME: {bay_2_name.upper()}")
          break
        else:
          break
    elif choice.lower() == "keycard override":
      print("\n[NOTICE] USE OF THIS OVERRIDE IS FOR DIAGNOSTIC PURPOSES ONLY FOR SERVICE ENGINEERS\n")
      while True:
        yes_no_input = prompt("PROCEED? [Y/N] ")
        if yes_no_input.upper() == "Y":
          config["keycard_supplied"] = True
          print("KEYCARD OVERRIDE ENABLED")
          time.sleep(1)
          print("\nPLEASE REBOOT FOR MENU")
          time.sleep(1)
          break
        elif yes_no_input.upper() == "N":
          break
    elif choice.lower() == "hydrocontroller selfrepair":
      print("\nDIAGNOSTICS ON HYDROCONTROLLERS:\n")
      for shower_id, state in config["showers"].items():
        time.sleep(1)
        if state == ShowerState.BROKEN:
          print(f"SHOWER {shower_id} IN ERRORED STATE\nDIAGNOSING...")
          time.sleep(3)
          print("SELF REPAIR COMPLETE\n[NOTICE] ADDITIONAL PART REQUIRED. RECIPE SENT TO MFG UNIT\n")
          config["showers"][shower_id] = ShowerState.OFF
        else:
          print(f"SHOWER {shower_id} OPERATION NORMAL")
    elif choice.lower() == "hydrocontroller status":
      print("\nHYDROCONTROLLER STATUS\n")
      time.sleep(1)
      for shower_id, state in config["showers"].items():
        if state == ShowerState.ON:
          print(f"SHOWER {shower_id} [> ON ]")
        elif state == ShowerState.OFF:
          print(f"SHOWER {shower_id} [> OFF]")
        elif state == ShowerState.BROKEN:
          print(f"SHOWER {shower_id} [ERROR]")
    elif choice.lower() == "hydrocontroller override":
      print("\n[NOTICE] USE THIS OVERRIDE TO TURN ALL HYDRO VALVES ON OR OFF\n")
      while True:
        on_off_input = prompt(" [ON/OFF/eXit] ")
        if on_off_input.upper() == "ON":
          for shower_id, state in config["showers"].items():
            if state == ShowerState.BROKEN:
              print(f"SHOWER {shower_id} IN ERRORED STATE\nSKIPPING...")
              time.sleep(1)
            else:
              config["showers"][shower_id] = ShowerState.ON
          break
        elif on_off_input.upper() == "OFF":
          for shower_id, state in config["showers"].items():
            if state == ShowerState.BROKEN:
              print(f"SHOWER {shower_id} IN ERRORED STATE\nSKIPPING...")
              time.sleep(1)
            else:
              config["showers"][shower_id] = ShowerState.OFF
          break
        elif on_off_input.upper() == "X":
          break
      print("DONE\n")
    elif choice.lower() == 'exit':
      save_config_to_file(config, "config.json")
      quit()

if __name__ == '__main__':
  bootup()