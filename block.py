class Block:
 def __init__(self, shape):
  self.shape = shape
  self.array = []
  self.in_play = 1
  self.pos = [0,3]
   
  def getArray(self):
    return self.array 

  def blockCollision(self, dead_blocks):
    for dead_block in dead_blocks:
      if self.collision(dead_block):
        return True;
    return False;

  def collision(self, dead_block):
    

class I(Block):
  def __init__(self):
    Block.__init__(self,"I")
    self.array1 = [[1,1,1,1],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    self.array2 = [[0,1,0,0],
                   [0,1,0,0],
                   [0,1,0,0],
                   [0,1,0,0]]
    self.arrays = [array1, array2]
    self.array = 0


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
    self.arrays = [array1, array2, array3, array4]
    self.array = 0

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
    self.arrays = [array1, array2, array3, array4]
    self.array = 0

class O(Block):
  def __init__(self):
    Block.__init__(self,"O")
    self.array1 = [[4,4,0,0],
                  [4,4,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    self.arrays = [self.array1]
    self.array = 0

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
    self.arrays = [array1, array2, array3, array4]
    self.array = 0
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
    self.arrays = [array1, array2]
    self.array = 0
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
    self.arrays = [array1, array2]
    self.array = 0
