#!/usr/bin/env python3 

import block, random, os, pygame, time
from board import init, getDead, setDead, getPos, setPos, setDeadRow, printDead, printBoard


class Tetris:
  def __init__(self):
    pygame.init()
  
  def start(self):
    init()
    self.done = False
    self.block_shapes = ["I","L","J","O","T","S","Z"]
    self.block = self.getBlock()
    self.array = self.block.arrays[self.block.array]
    self.screen = pygame.display.set_mode((200,400))
    self.last_moved = time.time()
    self.movement_delay = 0.3
    self.height = 20
    self.width = 10
    self.songs = ["TranceTechno.wav", "2PMTetris.wav", "TetrisBass.wav", "TetrisSong.wav", "TetrisAmazing.wav", "TetrisTheme.wav", "TetrisDacav.wav"]
    clock = pygame.time.Clock()
    FPS = 30
    while not(self.done):
      clock.tick(FPS)
      self.events()
      self.update()
      self.display()

  def clearGlitch(self):
    global dead_blocks
    number = None
    array = self.block.arrays[self.block.array]
    for i in range(4):
      for j in range(4):
        if array[i][j] != 0:
          number = array[i][j]
    points_on_top = self.block.pointsOnTop()
    print(points_on_top)
    for point in points_on_top:
      num = 0
      for row in range(point[0]):
        if getDead(row, point[1]) == number:
          num += 1
      if num == point[0]:
        printDead()
        print("clearing")
        for i in range(point[0]):
          print([i,point[1]])
          setDead(i,point[1],0)

  def fullLine(self):
    full = None 
    for row in range(self.height):
      not_zero = 0
      for col in range(self.width):
        if getDead(row,col) != 0:
          not_zero += 1
        if not_zero == self.width:
          print("full line")
          for col2 in range(self.width):
            setDead(row,col2,0)
          for row2 in range(row, 0, -1):
            setDeadRow(row2, row2-1)
          for col2 in range(self.width):
            setDead(0, col2, 0)

  def blockToBoard(self, oblock):
    array = oblock.arrays[oblock.array]
    for row in range(4):
      for col in range(4):
        if array[row][col] != 0:
          setPos(oblock.pos[0]+row,oblock.pos[1]+col,array[row][col])
  
  def clearBoard(self):
    for row in range(self.height): 
      for col in range(self.width):
        setPos(row, col,0)
  
  def deadToBoard(self):
#    print("line 84")
#    printBoard()
#    printDead()
    for row in range(self.height):
      for col in range(self.width):
        setPos(row,col,getDead(row,col))
#    print("line 90")
#    printBoard()
#    printDead()

  def events(self):
    events =  pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.done = True
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
        if event.key == pygame.K_DOWN:
          self.block.drop()
        if event.key == pygame.K_p:
          self.pause()
        if event.key == pygame.K_ESCAPE:
          self.done = True

  def pause(self):
    done = False
    while not done:
      es = pygame.event.get()
      for e in es:
        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_p:
            done = True

  def checkMusic(self):
    if not pygame.mixer.music.get_busy():
      pygame.mixer.music.load(random.choice(self.songs))
      pygame.mixer.music.play()

  def update(self):
#    print("line 120")
#    printBoard()
#    printDead()
    self.deadToBoard()
#    print("line 127")
#    printBoard()
#    printDead()
    self.blockToBoard(self.block)
#    print("line 131")
#    printBoard()
#    printDead()
    if not self.block.blockCollision() and self.block.inBoundsDown(): 
      if time.time() - self.last_moved > self.movement_delay:
        self.block.pos[0] += 1;
        self.last_moved = time.time()
    else:
#      if self.block.pos[0] == 0:
#        self.pause()
      #print("line 147")
      #printDead()
      array = self.block.arrays[self.block.array]
      for row in range(4):
        for col in range(4):
          if array[row][col] != 0:
            #what happens here???!!!
            setDead(row+self.block.pos[0],col+self.block.pos[1],array[row][col])
      #print("line 155")
      #printDead()
      #self.clearGlitch()
      self.block = self.getBlock()
      self.array = self.block.arrays[self.block.array]
      self.fullLine()

  def display(self):
    self.screen.fill((0,0,0))
    for row in range(self.height):
      for col in range(self.width):
        val = getPos(row,col)
        rect = pygame.Rect(col*20, row*20, 20, 20)
        border = pygame.Rect(col*20, row*20, 20, 20)
        if val == 0:
          pygame.draw.rect(self.screen, (0,0,0), rect)
        elif val == 1:
          pygame.draw.rect(self.screen, (0,247,247), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        elif val == 2:
          pygame.draw.rect(self.screen, (250,176,2), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        elif val == 3:
          pygame.draw.rect(self.screen, (27,2,250), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        elif val == 4:
          pygame.draw.rect(self.screen, (238,250,2), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        elif val == 5:
          pygame.draw.rect(self.screen, (180,2,250), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        elif val == 6:
          pygame.draw.rect(self.screen, (2,250,40), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
        else:
          pygame.draw.rect(self.screen, (250,7,2), rect)
          pygame.draw.rect(self.screen, (255,255,255), border, 2) 
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


    
