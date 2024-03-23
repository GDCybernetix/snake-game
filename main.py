import pygame
import os
from food import Food
from snake import *
pygame.init()
bounds = (300,300)
window = pygame.display.set_mode((bounds))
pygame.display.set_caption("snek")
block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
font = pygame.font.SysFont('comicsans',40, True)
run = True
while run:
  pygame.time.delay(100) 

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  snake.move()
  snake.check_for_food(food)
  snake.check_tail_collision()
  window.fill((0,0,0))
  snake.draw(pygame, window)
  food.draw(pygame, window)
  pygame.display.update()

  key = pygame.key.get_pressed()
  if key[pygame.K_UP] or key[pygame.K_w]:
    snake.direction = Direction.UP
  elif key[pygame.K_DOWN] or key[pygame.K_s]:
    snake.direction = Direction.DOWN
  elif key[pygame.K_LEFT] or key[pygame.K_a]:
    snake.direction = Direction.LEFT
  elif key[pygame.K_RIGHT] or key[pygame.K_d]:
    snake.direction = Direction.RIGHT

  if snake.check_bounds() == True or snake.check_tail_collision() == True:
    text = font.render('Game Over', True, (255,255,255))
    window.blit(text, (40,100))
    pygame.display.update()
    pygame.time.delay(1000)
    snake.respawn()
    food.respawn()
    snake.set_score()

  if snake.check_score() >= 0:
    text = font.render('Score:'+ str(snake.check_score()), True, (255,255,255))
    window.blit(text,(10,10))
    pygame.display.update()
    # pygame.time.delay(1000)