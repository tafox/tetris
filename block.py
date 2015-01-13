class Block:
 def __init__(self, shape):
  self.shape = shape
  self.array = []
  self.in_play = 1
  self.pos = [0,3]
   
  def getArray(self):
    return self.array 

class I(Block):
  def __init__(self):
    Block.__init__(self,"I")
    self.array = [[1,1,1,1],
                  [0,0,0,0]]

class L(Block):
  def __init__(self):
    Block.__init__(self,"L")
    self.array = [[2,2,2,0],
                  [2,0,0,0]]

class J(Block):
  def __init__(self):
    Block.__init__(self,"J")
    self.array = [[3,3,3,0],
                  [0,0,3,0]]

class O(Block):
  def __init__(self):
    Block.__init__(self,"O")
    self.array = [[4,4,0,0],
                  [4,4,0,0]]

class T(Block):
  def __init__(self):
    Block.__init__(self,"T")
    self.array = [[5,5,5,0,],
                  [0,5,0,0]]
class S(Block):
  def __init__(self):
    Block.__init__(self,"S")
    self.array = [[0,6,6,0],
                  [6,6,0,0]]
class Z(Block):
  def __init__(self):
    Block.__init__(self,"Z")
    self.array = [[7,7,0,0], 
                  [0,7,7,0]]
    
