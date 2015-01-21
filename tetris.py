#!/usr/bin/env python3 

import block, random, os, pygame
from board import board, getPos, setPos, dead_blocks, setDead


class Tetris:
  def __init__(self):
    pygame.init()
  
  def start(self):
    global board
    global dead_blocks
    for row in range(20):
      new_row = []
      other_row = []
      for col in range(10):
        new_row.append(0)
        other_row.append(0)
      board.append(new_row)
      dead_blocks.append(other_row)
    self.done = False
    self.block_shapes = ["I","L","J","O","T","S","Z"]
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
    global dead_blocks
    full = None 
    for row in range(20):
      not_zero = 0
      for col in range(10):
        if dead_blocks[row][col] != 0:
          not_zero += 1
        if not_zero == 10:
          for col2 in range(10):
            dead_blocks[row][col2] = 0
          for row2 in range(row, 0, -1):
            dead_blocks[row2] = dead_blocks[row2-1]
          for col2 in range(10):
            dead_blocks[0][col2] = 0

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
  
  def deadToBoard(self):
    global board
    global dead_blocks
    print("dead")
    for row in dead_blocks:
      print(row)
    print("")
    for row in range(20):
      for col in range(10):
        board[row][col] = dead_blocks[row][col]

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
    global dead_blocks
    global board
    self.deadToBoard()
    self.blockToBoard(self.block)
    print("board")
    for row in board:
      print(row)
    print("")
    if not self.block.blockCollision() and self.block.inBoundsDown(): 
      self.block.pos[0] += 1;
    else:
      print("Collision")
      if self.block.pos[0] == 0:
        self.done = True
      print("board")
      for row in board:
        print(row)
      for row in range(20):
        for col in range(10):
          dead_blocks[row][col] = board[row][col] 
#      for row in range(4):
#        for col in range(4):
#          if self.array[row][col] != 0:
#            print("write to dead")
#            for row2 in dead_blocks:
#              print(row2)
#            print("end1")
#            print("row" + str(row) + " col " + str(col))
#            print(str(self.array[row][col]) + "assigning to" + str(dead_blocks[self.block.pos[0]+row][self.block.pos[1]+col]))
#            print(str(self.block.pos[0]) + "by" + str(self.block.pos[1]))
#            setDead(self.block.pos[0]+row, self.block.pos[1]+col, self.array[row][col])
#            print("dead2")
#            for row2 in dead_blocks:
#              print(row2)
#            print("board")
#            for row2 in board:
#              print(row2)
#            print("end2")
      self.block = self.getBlock()
      self.array = self.block.arrays[self.block.array]
      self.fullLine()
      print("end of update")
      print("dead")
      for row in dead_blocks:
        print(row)
      print("")

  def display(self):
    self.screen.fill((255,255,255))
    for row in range(20):
      for col in range(10):
        val = getPos(row,col)
        rect = pygame.Rect(col*20, row*20, 20, 20)
        if val == 0:
          pygame.draw.rect(self.screen, (255,255,255), rect)
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


    
