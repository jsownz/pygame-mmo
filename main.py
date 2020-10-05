# import pygame module
import pygame
import character
import player

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

if __name__ == "__main__":

  character_data = character.get_character()
  # initialize game
  pygame.init()

  # get native screen size
  screenInfo = pygame.display.Info()
  NATIVE_WIDTH = screenInfo.current_w # 800
  NATIVE_HEIGHT = screenInfo.current_h # 600

  # set screen dimensions
  SCREEN_WIDTH = NATIVE_WIDTH
  SCREEN_HEIGHT = NATIVE_HEIGHT

  # create screen object
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

  # set window caption
  pygame.display.set_caption("Ninja Trainer")

  Clock = pygame.time.Clock()

  # set character stuff
  characterWidth = 40
  characterHeight = 60
  velocity = 25

  try:
    characterX = character_data["characterX"]
  except KeyError:
    characterX = 50

  try:
    characterY = character_data["characterY"]
  except KeyError:
    characterY = 50

  try:
    characterLevel = character_data["characterLevel"]
  except KeyError:
    characterLevel = 1

  try:
    characterXP = character_data["characterXP"]
  except KeyError:
    characterXP = 0

  # print out characters info
  print(f'Position: {characterX}, {characterY}, Level: {characterLevel}, XP: {characterXP}')


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
        
        # directional
        # add WASD
        if event.key == K_UP or event.key == K_w:
          # up
          print("move up")
          characterY -= velocity

        if event.key == K_DOWN or event.key == K_s:
          # down
          print("move down")
          characterY += velocity

        if event.key == K_LEFT or event.key == K_a:
          # left
          print("move left")
          characterX -= velocity

        if event.key == K_RIGHT or event.key == K_d:
          # right
          print("move right")
          characterX += velocity

        if event.key == K_x:
          player.earn_xp(100)
      
      # click the close button
      if event.type == QUIT:
        running = False

    screen.fill((0,0,0))
    characterRect = pygame.draw.rect(screen, (255, 0, 0), (characterX, characterY, characterWidth, characterHeight))
    pygame.display.update()

    loopCounter += 1
    if loopCounter % 300 == 0:
      character.store_info([{'characterX': characterRect.x, 'characterY': characterRect.y}])

    Clock.tick(30)