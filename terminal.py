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
  print ("""  > DIAGNOSTICS
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
      menu1()
    elif choice.lower() == 'controls':
      menu2()
    elif choice.lower() == 'roster':
      menu2()
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
  choice = input("PRESS RETURN")
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
< BACK""")
  choice = input("PRESS RETURN TO CONTINUE")
  if choice:
    option_diagnostics()



if __name__ == '__main__':
  bootup()