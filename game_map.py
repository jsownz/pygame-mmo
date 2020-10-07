import character

def transition(SCREEN_HEIGHT, SCREEN_WIDTH, characterWidth, characterHeight, planet_id, map_id, x, y):
  print(f'Planet_id: {planet_id}, map_id: {map_id}, x: {x}, y: {y}')
  if planet_id == 1:
    if map_id == 1:
      if y == 0 and x > (SCREEN_WIDTH-characterWidth):
        print(f'right spot')
        characterMapId = 2
        character.store_info([{'map_id': characterMapId, 'planet_id': planet_id}])
        return characterMapId
      else:
        return map_id
    else:
      return map_id
  else:
    return map_id