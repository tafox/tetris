import pygame, random, math

class Block:
  def __init__(self, position, shape):
    self.shape = shape
    self.position = position
    self.speed = 5
    self.in_play = 1
    if shape == "T":
      self.center = [position[0]+22.5,position[1]+15]
      self.vertices = [position,
                      [position[0]+45,position[1]],
                      [position[0]+45,position[1]+15],
                      [position[0]+30,position[1]+15],
                      [position[0]+30,position[1]+30],
                      [position[0]+15,position[1]+30],
                      [position[0]+15,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [222,48,193]
    if shape == "I": 
      self.center = [position[0]+30,position[1]+7.5]
      self.vertices = [position,
                      [position[0]+15,position[1]],
                      [position[0]+30,position[1]],
                      [position[0]+45,position[1]],
                      [position[0]+60,position[1]],
                      [position[0]+60,position[1]+15],
                      [position[0]+45,position[1]+15],
                      [position[0]+30,position[1]+15],
                      [position[0]+15,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [69,226,243]
    if shape == "J":
      self.center = [position[0]+22.5,position[1]+15]
      self.vertices = [position,
                      [position[0]+15,position[1]],
                      [position[0]+30,position[1]],
                      [position[0]+45,position[1]],
                      [position[0]+45,position[1]+15],
                      [position[0]+30,position[1]+15],
                      [position[0]+15,position[1]+15],
                      [position[0]+15,position[1]+30],
                      [position[0],position[1]+30]]
      self.color = [26,33,232]
    if shape == "L":
      self.center = [position[0]+22.5,position[1]+15]
      self.vertices = [position,
                      [position[0]+15,position[1]],
                      [position[0]+30,position[1]],
                      [position[0]+45,position[1]],
                      [position[0]+45,position[1]+15],
                      [position[0]+30,position[1]+15],
                      [position[0]+15,position[1]+15],
                      [position[0]+15,position[1]+30],
                      [position[0],position[1]+30],
                      [position[0],position[1]+15]]
      self.color = [238,152,5]
    if shape == "O":
      self.center = [position[0]+15,position[1]+15]
      self.vertices = [position,
                      [position[0]+15,position[1]],
                      [position[0]+30,position[1]],
                      [position[0]+30,position[1]+15],
                      [position[0]+30,position[1]+30],
                      [position[0]+15,position[1]+30],
                      [position[0],position[1]+30],
                      [position[0],position[1]+15]]
      self.color = [230,255,0]
    if shape == "S":
      self.center = [position[0]+0,position[1]+15]
      self.vertices = [position,  
                      [position[0]+30,position[1]],
                      [position[0]+30,position[1]+15],
                      [position[0]+15,position[1]+15],
                      [position[0]+15,position[1]+30],
                      [position[0]-15,position[1]+30],
                      [position[0]-15,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [0,255,26]
    if shape == "Z":
      self.center = [position[0]+30,position[1]+15]
      self.vertices = [position,  
                      [position[0]+30,position[1]], 
                      [position[0]+30,position[1]+15], 
                      [position[0]+45,position[1]+15],
                      [position[0]+45,position[1]+30],
                      [position[0]+15,position[1]+30],
                      [position[0]+15,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [233,0,39]
    
  def rotate_acw(self):
    for vertex in self.vertices:
      x = vertex[0] - self.center[0]
      y = vertex[1] - self.center[1] 
      vertex[0] = (x*math.cos(math.pi/2) - y*math.sin(math.pi/2)) + self.center[0]
      vertex[1] = (x*math.sin(math.pi/2) + y*math.cos(math.pi/2)) + self.center[1]

  def rotate_cw(self):
    for vertex in self.vertices:
      x = vertex[0] - self.center[0]
      y = vertex[1] - self.center[1]
      vertex[0] = (x*math.cos(math.pi/2)+y*math.sin(math.pi/2)) + self.center[0]
      vertex[1] = (x*-math.sin(math.pi/2)+y*math.cos(math.pi/2)) + self.center[1]

class DeadBlocks:
  def __init__(self):
    self.blocks = []   
