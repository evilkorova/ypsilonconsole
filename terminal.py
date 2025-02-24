from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import time

config = {
  "life_support_on": True,
  "keycard_supplied": False,
  "shower_1_on": False,
  "shower_2_on": False,
  "shower_3_on": False,
  "shower_4_on": False,
  "shower_5_on": False,
  "dock_1_locked": True,
  "dock_1_ship": "Heracles",
  "dock_2_locked": False,
  "dock_2_ship": "Grasshopper",
  "mineshaft_locked": False
}


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
      main_menu()
    else:
      print ("INVALID COMMAND")
      time.sleep(1)
      option_airlocks()

def option_showers():
  global config
  print ("\nTOGGLE WHICH SHOWER?")
  if GlobalVariables["shower_1_on"] == True:
    print ("SHOWER 1 [> ON]")
  else:
    print ("SHOWER 1 [> OFF]")
  if GlobalVariables["shower_2_on"] == True:
    print ("SHOWER 2 [> ON]")
  else:
    print ("SHOWER 2 [> OFF]")
  if GlobalVariables["shower_3_on"] == True:
    print ("SHOWER 3 [> ON]")
  else:
    print ("SHOWER 3 [> OFF]")
  if GlobalVariables["shower_4_on"] == True:
    print ("SHOWER 4 [> ON]")
  else:
    print ("SHOWER 4 [> OFF]")
  if GlobalVariables["shower_5_on"] == True:
    print ("SHOWER 5 [> ON]")
  else:
    print ("SHOWER 5 [> OFF]")
  print ("> ALL")
  print ("< BACK")
  menu_completer = WordCompleter(['ALL', 'BACK'], ignore_case=True)
  while True:
    choice = prompt('>>> ', completer=menu_completer)
    if choice.lower() == 'exit':
      break
    if choice.lower() == 'docking bay 1':

if __name__ == '__main__':
  bootup()