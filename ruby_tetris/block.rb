class Block
  attr_reader :pos
  def initialize
    @pos = [0,3]
  end

  def getArray
    return @arrays[@array]
  end
  
  def pointsToCheck
    array = self.getArray
    pp array
    points_to_check = []
    if array[0][0] == 1 and array[1][0] == 1
      return [[3+@pos[0],@pos[1]]]
    end
    for row in 0...3
      for col in 0...4
        if array[row][col] != 0 and array[row+1][col] == 0
          points_to_check.push([@pos[0]+row, @pos[1]+col])
        end
      end
    end
    return points_to_check
  end

  def pointsOnTop
    array = @arrays[@array]
    points_on_top = []
    for row in 0...4
      for col in 0...4
        if array[row][col] != 0 and (row == 0 or array[row-1][col] == 0)
          points_on_top.push([@pos[0]+row, @pos[1]+col])
        end
      end
    end
    return points_on_top
  end
  
  def drop
    points_to_check = self.pointsToCheck
    for i in 0...20
      for point in points_to_check
        if point[0]+i == 20 or $dead[point[0]+i][point[1]] != 0
          @pos[0] += (i-1)
          return
        end
      end
    end
  end

  def blockCollision
    points_to_check = self.pointsToCheck
    last_row = points_to_check[-1][0]
    for point in points_to_check
      if $board[point[0]+1][point[1]] != 0
        return true
      end
    end
    return false
  end

  def rotate
    if @array+1 == @arrays.length
      @array = 0
    else
      @array += 1
    end
  end

  def inboundsLeft
    points_to_check = self.pointsToCheck
    for point in points_to_check
      if point[1] == 0
        return false
      end
    end
    return true
  end

  def inboundsRight
    points_to_check = self.pointsToCheck
    for point in points_to_check
      if point[1] == 9
        return false
      end
    end
    return true
  end

  def inboundsDown
    points_to_check = self.pointsToCheck
    for point in points_to_check
      if point[0] == 19
        return false
      end
    end
    return true
  end
end

class I < Block
  def initialize
    super
    @array1 = [[1,1,1,1],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[1,0,0,0],
               [1,0,0,0],
               [1,0,0,0],
               [1,0,0,0]]
    @arrays = [@array1, @array2]
    @array = 0
  end
end

class L < Block
  def initialize 
    super
    @array1 = [[2,2,2,0],
               [2,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[2,2,0,0],
               [0,2,0,0],
               [0,2,0,0],
               [0,0,0,0]]
    @array3 = [[0,0,2,0],
               [2,2,2,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array4 = [[2,0,0,0],
               [2,0,0,0],
               [2,2,0,0],
               [0,0,0,0]]
    @arrays = [@array1, @array2, @array3, @array4]
    @array = 0
  end
end

class J < Block
  def initialize
    super
    @array1 = [[3,3,3,0],
               [0,0,3,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[0,3,0,0],
               [0,3,0,0],
               [3,3,0,0],
               [0,0,0,0]]
    @array3 = [[3,0,0,0],
               [3,3,3,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array4 = [[3,3,0,0],
               [3,0,0,0],
               [3,0,0,0],
               [0,0,0,0]]
    @arrays = [@array1, @array2, @array3, @array4]
    @array = 0
  end
end

 class O < Block
  def initialize 
    super
    @array1 = [[4,4,0,0],
               [4,4,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    @arrays = [@array1]
    @array = 0
  end
end

class T < Block
  def initialize 
    super
    @array1 = [[5,5,5,0,],
               [0,5,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[0,5,0,0,],
               [5,5,0,0],
               [0,5,0,0],
               [0,0,0,0]]
    @array3 = [[0,5,0,0,],
               [5,5,5,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array4 = [[5,0,0,0,],
               [5,5,0,0],
               [5,0,0,0],
               [0,0,0,0]]
    @arrays = [@array1, @array2, @array3, @array4]
    @array = 0
  end
end

class S < Block
  def initialize
    super
    @array1 = [[0,6,6,0],
               [6,6,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[6,0,0,0],
               [6,6,0,0],
               [0,6,0,0],
               [0,0,0,0]]
    @arrays = [@array1, @array2]
    @array = 0
  end
end

class Z < Block
  def initialize 
    super
    @array1 = [[7,7,0,0], 
               [0,7,7,0],
               [0,0,0,0],
               [0,0,0,0]]
    @array2 = [[0,7,0,0],
               [7,7,0,0],
               [7,0,0,0],
               [0,0,0,0]]
    @arrays = [@array1, @array2]
    @array = 0
  end
end
