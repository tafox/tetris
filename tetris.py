#!/usr/bin/env python3

import board, block, random, os

clear = lambda: os.system('clear')

class Tetris:
  def __init__(self):
    pass
  
  def start(self):
    self.done = False
    self.board = board.Board(10,20)
    self.block_shapes = ["I","L","J","O","T","S","Z"]
    self.dead_blocks = []
    self.spawn_point = [0,3]
    self.block = self.getBlock()
    while not(self.done):
      self.update()
      self.display()

  def blockToBoard(self, oblock):
    for row in range(2):
      for col in range(4):
        self.board.setBoardPos((self.block.pos[0]+row,oblock.pos[1]+col),oblock.array[row][col])
  
  def clearBlock(self):
    for row in range(2):
      for col in range(4):
        self.board.setBoardPos((self.block.pos[0]+row-1,self.block.pos[1]+col),0)

  def update(self):
    self.clearBlock()
    self.blockToBoard(self.block)
    for dead_block in self.dead_blocks:
      self.blockToBoard(dead_block)
    if self.block.pos[0] < 17:
      self.block.pos[0] += 1 
    else:
      self.dead_blocks.append(self.block)
      self.block = self.getBlock()
  
  def display(self):
    clear()
    print(self.board)

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

    
