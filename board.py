class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = []
    for i in range(self.height):
      row = []
      for j in range(self.width):
        row.append(0)
      self.board.append(row)

  def setBoardPos(self,pos,val):
    self.board[pos[0]][pos[1]] = val

  def __str__(self):
    output = ""
    for i in range(20):
      output += str(self.board[i]) + '\n'
    return output

  


            
        
        

  




