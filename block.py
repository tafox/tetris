class Block:
  def __init__(self, shape):
    self.shape = shape
    self.array = 0;
    self.arrays = []
    self.in_play = 1
    self.pos = [0,3]
    self.board = []
   
  def getArray(self):
    return self.array 

  def blockCollision(self, dead_blocks):
    for dead_block in dead_blocks:
      if self.collision(dead_block):
        return True
    return False

  def pointsToCheck(self):
    points_to_check = []
    for row in range(3):
      blanks = 0
      for col in range(4):
        if self.board.getBoardPos([self.pos[0]+row,self.pos[1]+col]) != 0:
          points_to_check.append([self.pos[0]+row, self.pos[1]+col])
        else:
          blanks+= 1
        if blanks == 4:
          return points_to_check
    return points_to_check

  def collision(self, dead_block):
    points_to_check = self.pointsToCheck()
    last_row = points_to_check[-1][0]
    for point in points_to_check:
      if point[0] == last_row:
        if self.board.getBoardPos([point[0]+1,point[1]]) != 0:
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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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
    
  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

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

  def blockCollision(self, dead_blocks):
    return Block.blockCollision(self, dead_blocks)

  def pointsToCheck(self):
    return Block.pointsToCheck(self)

  def collision(self, dead_block):
    return Block.collision(self, dead_block)

  def rotate(self):
    return Block.rotate(self)

  def inBoundsLeft(self):
    return Block.inBoundsLeft(self)

  def inBoundsRight(self):
    return Block.inBoundsRight(self)

  def inBoundsDown(self):
    return Block.inBoundsDown(self)

