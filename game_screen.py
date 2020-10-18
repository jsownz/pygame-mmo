import pygame
import config
import character

def update_screen(screen, color, x, y, width, height):
  screen.fill((0,0,0))
  characterRect = pygame.draw.rect(screen, color, (x, y, width, height))
  pygame.display.update()

  config.loopCounter += 1
  if config.loopCounter % 150 == 0:
    character.store_info([{'x': characterRect.x, 'y': characterRect.y}])