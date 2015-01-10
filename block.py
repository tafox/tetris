import pygame, random

class Block:
  def __init__(self, position, shape):
    self.shape = shape
    self.position = position
    self.speed = 5
    self.in_play = 1
    if shape == "T":
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
      self.vertices = [position,
                      [position[0]+60,position[1]],
                      [position[0]+60,position[1]+15],
                      [position[0], position[1]+15]]
      self.color = [69,226,243]
    if shape == "J":
      self.vertices = [position,
                      [position[0]+45,position[1]],
                      [position[0]+45,position[1]+15],
                      [position[0]+15,position[1]+15],
                      [position[0]+15,position[1]+30],
                      [position[0],position[1]+30]]
      self.color = [26,33,232]
    if shape == "L":
      self.vertices = [position,
                      [position[0]+45,position[1]],
                      [position[0]+45,position[1]+30],
                      [position[0]+30,position[1]+30],
                      [position[0]+30,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [238,152,5]
    if shape == "O":
      self.vertices = [position,
                      [position[0]+30,position[1]],
                      [position[0]+30,position[1]+30],
                      [position[0],position[1]+30]]
      self.color = [230,255,0]
    if shape == "S":
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
      self.vertices = [position,  
                      [position[0]+30,position[1]], 
                      [position[0]+30,position[1]+15], 
                      [position[0]+45,position[1]+15],
                      [position[0]+45,position[1]+30],
                      [position[0]+15,position[1]+30],
                      [position[0]+15,position[1]+15],
                      [position[0],position[1]+15]]
      self.color = [233,0,39]
    
