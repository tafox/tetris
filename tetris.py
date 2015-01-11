#!/usr/bin/env python3

import pygame, sys, random
from block import Block, DeadBlocks

class Tetris:
  def __init__(self):
    pygame.init()
    self.surface_width = 640
    self.surface_height = 480
    self.surface_center = [int(self.surface_width/2),int(self.surface_height/2)]
    self.box_color = [64,79,218]
    self.box_left1 = [self.surface_center[0]-77.5,self.surface_center[1]+152.5]
    self.box_left2 = [self.surface_center[0]-77.5,self.surface_center[1]-152.5]
    self.box_right1 = [self.surface_center[0]+77.5,self.surface_center[1]+152.5]
    self.box_right2 = [self.surface_center[0]+77.5,self.surface_center[1]-152.5]
    self.done = False
    self.surface = pygame.display.set_mode([self.surface_width,self.surface_height])
    self.block = None
    self.dead = DeadBlocks()
  
  def event_update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sys.exit()
        if event.key == pygame.K_LEFT:
          for vertex in self.block.vertices:
            if vertex[0] <= self.box_left1[0]+2.5:
              return 
          self.block.center[0] -= 15
          for vertex in self.block.vertices:
            vertex[0] -= 15
        if event.key == pygame.K_RIGHT:
          for vertex in self.block.vertices:
            if vertex[0] >= self.box_right1[0]-2.5:
              return
          self.block.center[0] += 15
          for vertex in self.block.vertices:
            vertex[0] += 15
        if event.key == pygame.K_UP:
          self.block.rotate_acw()
        if event.key == pygame.K_DOWN:
          self.block.rotate_cw()

  def game_update(self):
    self.surface.fill([0,0,0]) 
    pygame.draw.line(self.surface,self.box_color,self.box_left1,self.box_right1,5)
    pygame.draw.line(self.surface,self.box_color,self.box_left1,self.box_left2,5)
    pygame.draw.line(self.surface,self.box_color,self.box_right1,self.box_right2,5)

    for vertex in self.block.vertices:
      if vertex[1] >= self.surface_center[1]+150:
        self.block.speed = 0
        self.block.in_play = 0
      for dead_block in self.dead.blocks:
        for dead_vertex in dead_block.vertices:
          if vertex == dead_vertex:
            self.block.speed = 0
            self.block.in_play = 0
      if vertex[1] < self.surface_center[1]-150:
        done = True
    
    if not(self.block.in_play):
      self.dead.blocks.append(self.block)
      self.block = self.get_block() 

    pygame.draw.polygon(self.surface,self.block.color,self.block.vertices)
    
    self.block.center[1] += self.block.speed
    for vertex in self.block.vertices:
      vertex[1] += self.block.speed
      for dead_block in self.dead.blocks:
        pygame.draw.polygon(self.surface,dead_block.color,dead_block.vertices)
    
  
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
game.block = game.get_block()

while not(game.done):
  game.game_update()
  game.event_update()
  pygame.display.update()
  
