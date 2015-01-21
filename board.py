board = []
dead_blocks = []

def setPos(row, col, val):
  global board
  if 19 < row or row < 0:
    return 
  if 9 < col or col < 0:
    return 
  board[row][col] = val

def getPos(row,col):
  global board
  if 19 < row or row  < 0:
    return 0
  if 9 < col or col < 0:
    return 0
  return board[row][col]

def setDead(row, col, val):
  global dead_blocks
  dead_blocks[row][col] = val

