import json
import os
from enum import Enum

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
  
config = load_config_from_file("config.json", default_config)

def register_ship(ship_var):
  global config
  name = config[ship_var]
  print(f"\nREGISTERED SHIP FOR {ship_var} IS {name}")
  new_name = input(f"NEW NAME OR ENTER TO CANCEL [{name}]> ")
  if new_name:
    config[ship_var] = new_name.upper()
    print(f"\nREGISTERED NEW NAME: {new_name.upper()}")

    

def main():
  register_ship("dock_1_ship")
  register_ship("dock_2_ship")
  save_config_to_file(config, "config.json")


if __name__ == '__main__':
  main()