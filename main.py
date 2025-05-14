import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  clock = pygame.time.Clock()
  dt = 0
  display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(display, color=(0,0,0))
    player.draw(screen=display)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()