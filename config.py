import pygame

from pygame.locals import (
  FULLSCREEN,
)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
characterHeight = 60
characterWidth = 40
velocity = 25

pygame.init()

# get native screen size
screenInfo = pygame.display.Info()
NATIVE_WIDTH = screenInfo.current_w # 800
NATIVE_HEIGHT = screenInfo.current_h # 600

# set screen dimensions
SCREEN_WIDTH = NATIVE_WIDTH
SCREEN_HEIGHT = NATIVE_HEIGHT

# create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)

# set window caption
pygame.display.set_caption("Ninja Trainer")

Clock = pygame.time.Clock()