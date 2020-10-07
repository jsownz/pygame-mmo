# import pygame module
import pygame
import character
import player
import game_map

# import locals for key coordinates
from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  K_w,
  K_a,
  K_s,
  K_d,
  K_x,
  KEYDOWN,
  QUIT,
)

from config import (
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  characterHeight,
  characterWidth,
  velocity,
  screen,
  Clock
)

if __name__ == "__main__":

  character_data = character.get_character()

  try:
    characterX = character_data["x"]
  except KeyError:
    characterX = 50

  try:
    characterY = character_data["y"]
  except KeyError:
    characterY = 50

  try:
    characterLevel = character_data["level"]
  except KeyError:
    characterLevel = 1

  try:
    characterXP = character_data["xp"]
  except KeyError:
    characterXP = 0
  
  try:
    characterPlanetId = character_data["planet_id"]
  except KeyError:
    characterPlanetId = 1
  
  try:
    characterMapId = character_data["map_id"]
  except KeyError:
    characterMapId = 1

  # print out characters info
  print(f'Position: {characterX}, {characterY}, Level: {characterLevel}, XP: {characterXP}')

  def map_transition(planet_id, map_id, x, y):
    global characterMapId
    print(f'Planet_id: {planet_id}, map_id: {map_id}, x: {x}, y: {y}')
    if planet_id == 1:
      if map_id == 1:
        if y == 0 and x > (SCREEN_WIDTH-characterWidth):
          print(f'right spot')
          characterMapId = 2
          character.store_info([{'map_id': characterMapId, 'planet_id': characterPlanetId}])

  loopCounter = 0

  # game loop variable
  running = True

  # main loop
  while running:
    
    # pygame.time.delay(10)

    # loop through events
    for event in pygame.event.get():
      # press a key?
      if event.type == KEYDOWN:
        # if escape, exit
        if event.key == K_ESCAPE:
          running = False

        if event.key == K_x:
          player.earn_xp(100)
      
      # click the close button
      if event.type == QUIT:
        running = False

    keys = pygame.key.get_pressed()
    
    # movement
    # up
    if keys[K_UP] or keys[K_w]:
      characterY -= velocity
      if characterY < 0:
        characterMapId = game_map.transition(SCREEN_HEIGHT, SCREEN_WIDTH, characterWidth, characterHeight, characterPlanetId, characterMapId, characterX, characterY)
        characterY = 0

    # down
    if keys[K_DOWN] or keys[K_s]:
      characterY += velocity
      if characterY+characterHeight > SCREEN_HEIGHT:
        characterMapId = game_map.transition(SCREEN_HEIGHT, SCREEN_WIDTH, characterWidth, characterHeight, characterPlanetId, characterMapId, characterX, characterY)
        characterY = SCREEN_HEIGHT-characterHeight

    # left
    if keys[K_LEFT] or keys[K_a]:
      characterX -= velocity
      if characterX < 0:
        characterMapId = game_map.transition(SCREEN_HEIGHT, SCREEN_WIDTH, characterWidth, characterHeight, characterPlanetId, characterMapId, characterX, characterY)
        characterX = 0

    # right
    if keys[K_RIGHT] or keys[K_d]:
      characterX += velocity
      if characterX+characterWidth > SCREEN_WIDTH:
        characterMapId = game_map.transition(SCREEN_HEIGHT, SCREEN_WIDTH, characterWidth, characterHeight, characterPlanetId, characterMapId, characterX, characterY)
        characterX = SCREEN_WIDTH-characterWidth


    screen.fill((0,0,0))
    characterRect = pygame.draw.rect(screen, (255, 0, 0), (characterX, characterY, characterWidth, characterHeight))
    pygame.display.update()

    loopCounter += 1
    if loopCounter % 150 == 0:
      character.store_info([{'x': characterRect.x, 'y': characterRect.y}])

    Clock.tick(30)