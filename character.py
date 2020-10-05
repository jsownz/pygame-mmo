import json
import pathlib

character_file = pathlib.Path(__file__).parent / 'character.json'
character_data = {}

def get_character():
    global character_data
    if character_file.exists():
      with open(character_file) as json_file:
        character_data = json.load(json_file)
    else:
      with open(character_file, 'w') as outfile:
        json.dump(character_data, outfile)

    return character_data

def store_info(info):
  global character_data

  for item in info:
    for key in item.keys():
      val = item[key]
      character_data[key] = val

  with open(character_file, 'w') as outfile:
    json.dump(character_data, outfile)
  print("Info saved.")