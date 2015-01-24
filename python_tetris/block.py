from board import getPos, setPos, setDead, getDead

class Block:
  def __init__(self, shape):
    self.shape = shape
    self.array = 0;
    self.arrays = []
    self.pos = [0,3]
   
  def getArray(self):
    return self.array 

  def pointsToCheck(self):
    array = self.arrays[self.array]
    points_to_check = []
    if array[0][0] == 1 and array[1][0] == 1:
      return [[3+self.pos[0],self.pos[1]]]
    for row in range(3):
      for col in range(4):
        if array[row][col] != 0 and array[row+1][col] == 0:
          points_to_check.append([self.pos[0]+row, self.pos[1]+col])
    return points_to_check

  def pointsOnTop(self):
    array = self.arrays[self.array]
    points_on_top = []
    for row in range(4):
      for col in range(4):
        if array[row][col] != 0 and (row == 0 or array[row-1][col] == 0):
          points_on_top.append([self.pos[0]+row, self.pos[1]+col])
    return points_on_top
  
  def drop(self):
    points_to_check = self.pointsToCheck()
    for i in range(20):
      for point in points_to_check:
        if point[0]+i == 20 or getDead(point[0]+i,point[1]) != 0:
          self.pos[0] += (i-1)
          return

  def blockCollision(self):
    points_to_check = self.pointsToCheck()
    last_row = points_to_check[-1][0]
    for point in points_to_check:
      if getPos(point[0]+1,point[1]) != 0:
        return True
    return False

  def rotate(self):
    if self.array+1 == len(self.arrays):
      self.array = 0
    else:
      self.array += 1

  def inBoundsLeft(self):
    points_to_check = self.pointsToCheck()
    for point in points_to_check:
      if point[1] == 0:
        return False
    return True

  def inBoundsRight(self):
    points_to_check = self.pointsToCheck()
    for point in points_to_check:
      if point[1] == 9:
        return False
    return True

  def inBoundsDown(self):
    points_to_check = self.pointsToCheck()
    for point in points_to_check:
      if point[0] == 19:
        return False
    return True

class I(Block):
  def __init__(self):
    Block.__init__(self,"I")
    self.array1 = [[1,1,1,1],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[1,0,0,0],
                   [1,0,0,0],
                   [1,0,0,0],
                   [1,0,0,0]]
    self.arrays = [self.array1, self.array2]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class L(Block):
  def __init__(self):
    Block.__init__(self,"L")
    self.array1 = [[2,2,2,0],
                   [2,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[2,2,0,0],
                   [0,2,0,0],
                   [0,2,0,0],
                   [0,0,0,0]]
    self.array3 = [[0,0,2,0],
                   [2,2,2,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array4 = [[2,0,0,0],
                   [2,0,0,0],
                   [2,2,0,0],
                   [0,0,0,0]]
    self.arrays = [self.array1, self.array2, self.array3, self.array4]
    self.array = 0
    
  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class J(Block):
  def __init__(self):
    Block.__init__(self,"J")
    self.array1 = [[3,3,3,0],
                   [0,0,3,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[0,3,0,0],
                   [0,3,0,0],
                   [3,3,0,0],
                   [0,0,0,0]]
    self.array3 = [[3,0,0,0],
                   [3,3,3,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array4 = [[3,3,0,0],
                   [3,0,0,0],
                   [3,0,0,0],
                   [0,0,0,0]]
    self.arrays = [self.array1, self.array2, self.array3, self.array4]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class O(Block):
  def __init__(self):
    Block.__init__(self,"O")
    self.array1 = [[4,4,0,0],
                  [4,4,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    self.arrays = [self.array1]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class T(Block):
  def __init__(self):
    Block.__init__(self,"T")
    self.array1 = [[5,5,5,0,],
                   [0,5,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[0,5,0,0,],
                   [5,5,0,0],
                   [0,5,0,0],
                   [0,0,0,0]]
    self.array3 = [[0,5,0,0,],
                   [5,5,5,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array4 = [[5,0,0,0,],
                   [5,5,0,0],
                   [5,0,0,0],
                   [0,0,0,0]]
    self.arrays = [self.array1, self.array2, self.array3, self.array4]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class S(Block):
  def __init__(self):
    Block.__init__(self,"S")
    self.array1 = [[0,6,6,0],
                   [6,6,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[6,0,0,0],
                   [6,6,0,0],
                   [0,6,0,0],
                   [0,0,0,0]]
    self.arrays = [self.array1, self.array2]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

class Z(Block):
  def __init__(self):
    Block.__init__(self,"Z")
    self.array1 = [[7,7,0,0], 
                   [0,7,7,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[0,7,0,0],
                   [7,7,0,0],
                   [7,0,0,0],
                   [0,0,0,0]]
    self.arrays = [self.array1, self.array2]
    self.array = 0

  def blockCollision(self):
    return Block.blockCollision(self)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)
