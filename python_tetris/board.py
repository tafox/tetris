board = []
dead_blocks = []

def init():
  for row in range(20):
    new_row = []
    other_row = []
    for col in range(10):
      new_row.append(0)
      other_row.append(0)
    board.append(new_row)
    dead_blocks.append(other_row)

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
  printDead()
  print(val)
  print("["+str(row)+"]["+str(col)+"] = " + str(dead_blocks[row][col]))
  dead_blocks[row][col] = val
  print("["+str(row)+"]["+str(col)+"] = " + str(dead_blocks[row][col]))
  printDead()

def getDead(row, col):
  return dead_blocks[row][col]

def setDeadRow(row, row2):
  dead_blocks[row] = dead_blocks[row2]

def printBoard():
  print("Board")
  for row in range(20):
    print(str(board[row])+ str(row))

def printDead():
  print("Dead")
  for row in range(20):
    print(str(dead_blocks[row]) + str(row))
