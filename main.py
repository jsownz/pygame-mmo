# import pygame module
import pygame
import character
import player
import game_map
import game_screen

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
  Clock,
  loopCounter
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


    game_screen.update_screen(screen, (255,0,0), characterX, characterY, characterWidth, characterHeight)

    Clock.tick(30)