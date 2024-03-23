from enum import Enum
import pygame
# score = 0
class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Snake:
  length = None
  direction = None
  body = None
  block_size = None
  color = (0,255,0)
  bounds = None
  def respawn(self):
    self.length = 3
    #establishing the default length of the snake
    self.body = [(20,20),(20,40),(20,60)]
    #contains coordinates of the snake body within a list to extend the snake. we will be appending to the list
    self.direction = Direction.DOWN

  def __init__(self, block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    #checking if the snake is going to go out of bounds
    self.respawn()
    self.score = 0


  def draw(self, game, window):
    for segment in self.body:
      game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))
  
  def move(self):
    curr_head = self.body[-1]
    if self.direction == Direction.DOWN:
      next_head = (curr_head[0], curr_head[1] + self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.UP:
      next_head = (curr_head[0], curr_head[1] - self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.RIGHT:
      next_head = (curr_head[0] + self.block_size, curr_head[1])
      self.body.append(next_head)
    elif self.direction == Direction.LEFT:
      next_head = (curr_head[0] - self.block_size, curr_head[1])
      self.body.append(next_head)

    if self.length < len(self.body):
      self.body.pop(0)

  def steer(self, direction):
    if direction == Direction.DOWN and self.direction != Direction.UP:
      self.direction = Direction.DOWN 
    elif direction == Direction.UP and self.direction != Direction.DOWN:
      self.direction = Direction.UP
    elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
      self.direction = Direction.RIGHT
    elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
      self.direction = Direction.LEFT

  def eat(self):
      self.length += 1
  
  def check_for_food(self,food):
    head = self.body[-1]
    if head[0] == food.x and head[1] == food.y:
      self.eat()
      food.respawn()
      self.score += 1
      # score += 1


  def check_tail_collision(self):
    head = self.body[-1]
    has_eaten_tail = False

    for i in range(len(self.body) - 1):
      segment = self.body[i]
      if head[0] == segment[0] and head[1] == segment[1]:
        has_eaten_tail = True

    return has_eaten_tail
  
  def check_bounds(self):
    head = self.body[-1]
    if head[0] >= self.bounds[0]:
      return True
    if head[1] >= self.bounds[1]:
      return True

    if head[0] < 0:
        return True
    if head[1] < 0:
        return True

    return False
  def check_score(self):
    return self.score
  def set_score(self):
    self.score = 0