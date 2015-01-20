#!/usr/bin/env python3 

import board, block, random, os, pygame

clear = lambda: os.system('clear')

class Tetris:
  def __init__(self):
    pygame.init()
  
  def start(self):
    self.done = False
    self.board = board.Board(10,20)
    self.block_shapes = ["I","L","J","O","T","S","Z"]
    self.dead_blocks = []
    self.spawn_point = [0,3]
    self.block = self.getBlock()
    self.array = self.block.arrays[self.block.array]
    self.screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    FPS = 10
    while not(self.done):
      clock.tick(FPS)
      pygame.event.get()
      self.events()
      self.update()
      self.display()

  def blockToBoard(self, oblock):
    array = oblock.arrays[oblock.array]
    for row in range(4):
      for col in range(4):
        if array[row][col] != 0:
          self.board.setBoardPos((oblock.pos[0]+row,oblock.pos[1]+col),array[row][col])
  
  def clearBlock(self):
    for col in range(4): 
      for row in range(4):
        if self.array[row][col] != 0:
          self.board.setBoardPos((self.block.pos[0]+row-1,self.block.pos[1]+col),0)

  def events(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      if self.block.inBoundsLeft():
        self.block.pos[1] -= 1
    if keys[pygame.K_RIGHT]:
      if self.block.inBoundsRight():
        self.block.pos[1] += 1
    if keys[pygame.K_UP]:
      self.block.rotate()
      self.array = self.block.arrays[self.block.array]
    if keys[pygame.K_ESCAPE]:
      self.done = True

  def update(self):
    self.clearBlock()
    self.blockToBoard(self.block)
    for dead_block in self.dead_blocks:
      self.blockToBoard(dead_block)
    self.block.board = self.board
    if not self.block.blockCollision(self.dead_blocks) and self.block.inBoundsDown(): 
      self.block.pos[0] += 1;
    else:
      if self.block.pos[0] == 0:
        self.done = True
      self.dead_blocks.append(self.block)
      self.block = self.getBlock()
      self.array = self.block.arrays[self.block.array]
      self.block.board = self.board

  def display(self):
    self.screen.fill((0,0,255))
    for row in range(20):
      for col in range(10):
        val = self.board.getBoardPos([row,col])
        rect = pygame.Rect(col*20, row*20, 10, 10)
        if val == 0:
          pygame.draw.rect(self.screen, (0,0,0), rect)
        else:
          pygame.draw.rect(self.screen, (255,0,0), rect)
    pygame.display.flip()

  def getBlock(self):
    rblock = random.choice(self.block_shapes)
    if rblock == "I":
      return block.I()
    elif rblock == "O":
      return block.O()
    elif rblock == "L":
      return block.L()
    elif rblock == "J":
      return block.J()
    elif rblock == "T":
      return block.T()
    elif rblock == "S":
      return block.S()
    elif rblock == "Z":
      return block.Z()
    else:
      print("Error invalid block")
   
game = Tetris()
game.start()

    
