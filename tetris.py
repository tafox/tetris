#!/usr/bin/env python3 

import block, random, os, pygame
from board import board, getPos, setPos


class Tetris:
  def __init__(self):
    pygame.init()
  
  def start(self):
    global board
    for row in range(20):
      new_row = []
      for col in range(10):
        new_row.append(0)
      board.append(new_row)
    self.done = False
    self.block_shapes = ["I","L","J","O","T","S","Z"]
    self.dead_blocks = []
    self.block = self.getBlock()
    self.array = self.block.arrays[self.block.array]
    self.screen = pygame.display.set_mode((200,400))
    clock = pygame.time.Clock()
    FPS = 5
    playtime = 0.0
    while not(self.done):
      clock.tick(FPS)
      self.events()
      self.update()
      self.display()

  def fullLine(self):
    global board
    full = None 
    for row in range(20):
      not_zero = 0
      for col in range(10):
        if getPos(row,col) != 0:
          not_zero += 1
        if not_zero == 10:
          full = row
    if full:
      for col in range(10):
        setPos(full, col, 0)
      for row in range(full, 0, -1):
        board[row] = board[row-1]
      for col in range(10):
        board[0][col] = 0

  def blockToBoard(self, oblock):
    array = oblock.arrays[oblock.array]
    for row in range(4):
      for col in range(4):
        if array[row][col] != 0:
          setPos(oblock.pos[0]+row,oblock.pos[1]+col,array[row][col])
  
  def clearBoard(self):
    for col in range(10): 
      for row in range(20):
        setPos(row, col,0)

  def events(self):
    events =  pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          if self.block.inBoundsLeft():
            self.block.pos[1] -= 1
        if event.key == pygame.K_RIGHT:
          if self.block.inBoundsRight():
            self.block.pos[1] += 1
        if event.key == pygame.K_UP:
          self.block.rotate()
          self.array = self.block.arrays[self.block.array]
        if event.key == pygame.K_ESCAPE:
          self.done = True

  def update(self):
    self.clearBoard()
    self.blockToBoard(self.block)
    for dead_block in self.dead_blocks:
      self.blockToBoard(dead_block)
    if not self.block.blockCollision() and self.block.inBoundsDown(): 
      self.block.pos[0] += 1;
    else:
      if self.block.pos[0] == 0:
        self.done = True
      self.dead_blocks.append(self.block)
      self.block = self.getBlock()
      self.array = self.block.arrays[self.block.array]
      self.fullLine()

  def display(self):
    self.screen.fill((0,0,0))
    for row in range(20):
      for col in range(10):
        val = getPos(row,col)
        rect = pygame.Rect(col*20, row*20, 20, 20)
        if val == 0:
          pygame.draw.rect(self.screen, (0,0,0), rect)
        elif val == 1:
          pygame.draw.rect(self.screen, (0,247,247), rect)
        elif val == 2:
          pygame.draw.rect(self.screen, (250,176,2), rect)
        elif val == 3:
          pygame.draw.rect(self.screen, (27,2,250), rect)
        elif val == 4:
          pygame.draw.rect(self.screen, (238,250,2), rect)
        elif val == 5:
          pygame.draw.rect(self.screen, (180,2,250), rect)
        elif val == 6:
          pygame.draw.rect(self.screen, (2,250,40), rect)
        else:
          pygame.draw.rect(self.screen, (250,7,2), rect)
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


    
