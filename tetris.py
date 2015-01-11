#!/usr/bin/env python3

import pygame, sys, random
from block import Block

class Tetris:
  def __init__(self):
    pygame.init()
    self.surface_width = 640
    self.surface_height = 480
    self.surface_center = [int(self.surface_width/2),int(self.surface_height/2)]
    self.surface = pygame.display.set_mode([self.surface_width,self.surface_height])
  
  def event_update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sys.exit()
        if event.key == pygame.K_LEFT:
          block.center[0] -= 15
          for vertex in block.vertices:
            vertex[0] -= 15
        if event.key == pygame.K_RIGHT:
          block.center[0] += 15
          for vertex in block.vertices:
            vertex[0] += 15
        if event.key == pygame.K_UP:
          block.rotate_acw()
        if event.key == pygame.K_DOWN:
          block.rotate_cw()

  
  def get_block(self):
    spawn_point = [self.surface_center[0], self.surface_center[1]-150]
    rand = random.randrange(1,7)
    if rand == 1:
      return Block(spawn_point,"I")
    if rand == 2:
      return Block(spawn_point,"J")
    if rand == 3:
      return Block(spawn_point,"L")
    if rand == 4:
      return Block(spawn_point,"O")
    if rand == 5:
      return Block(spawn_point,"S")
    if rand == 6:
      return Block(spawn_point,"T")
    if rand == 7:
      return Block(spawn_point,"Z")

game = Tetris()
done = False
box_color = [64,79,218]
block = game.get_block()
dead_blocks = []

while not(done):
  game.surface.fill([0,0,0]) 
  pygame.draw.line(game.surface,box_color,(game.surface_center[0]-75,game.surface_center[1]+150),(game.surface_center[0]+75,game.surface_center[1]+150),5)
  pygame.draw.line(game.surface,box_color,(game.surface_center[0]-75,game.surface_center[1]+150),(game.surface_center[0]-75,game.surface_center[1]-150),5)
  pygame.draw.line(game.surface,box_color,(game.surface_center[0]+75,game.surface_center[1]+150),(game.surface_center[0]+75,game.surface_center[1]-150),5)
  for vertex in block.vertices:
    if vertex[1] >= game.surface_center[1]+150:
      block.speed = 0
      block.in_play = 0
    if vertex[1] < game.surface_center[1]-165:
      done = True
    
  
  if not(block.in_play):
    dead_blocks.append(block)
    block = game.get_block() 
  pygame.draw.polygon(game.surface,block.color,block.vertices)
  
  block.center[1] += block.speed
  for vertex in block.vertices:
    vertex[1] += block.speed
  for dead_block in dead_blocks:
    pygame.draw.polygon(game.surface,dead_block.color,dead_block.vertices)
  game.event_update()
  pygame.display.update()
  

  game.event_update()
  pygame.display.update()
  
