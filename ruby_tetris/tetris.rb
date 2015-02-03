#!/usr/bin/env ruby

require 'pp'
require 'gosu'
require_relative 'block'

$board = []
$dead = []

def getBlock()
  num = rand(7) + 1
  if num == 1
    return I.new
  elsif num == 2
    return L.new
  elsif num == 3
    return J.new
  elsif num == 4
    return O.new
  elsif num == 5
    return T.new
  elsif num == 6
    return S.new
  else
    return Z.new
  end
end

class MyWindow < Gosu::Window
  def initialize
    super(200,400,false)
    self.caption = "Tetris"
    @font = Gosu::Font.new(self,"Arial",14)
    @board_height = 20
    @board_width = 10
    @square_length = 20
    for i in 0...@board_height
      row = []
      for j in 0...@board_width
        row.push(0)
      end
      $board.push(row)
    end
    for i in 0...@board_height
      row = []
      for j in 0...@board_width
        row.push(0)
      end
      $dead.push(row)
    end
    @movement_delay = 0.5
    @last_moved = Time.now
    @score = 0
    @block = getBlock()
  end

  def button_down(id)
    if id == Gosu::KbLeft and @block.inboundsLeft
      @block.pos[1] -= 1
    end
    if id == Gosu::KbRight and @block.inboundsRight
      @block.pos[1] += 1
    end
    if id == Gosu::KbUp
      @block.rotate
    end
    if id == Gosu::KbDown
      @block.drop
    end
    if id == Gosu::KbEscape
      close
    end
  end

  def update()
    if @block.inboundsDown and not @block.blockCollision
      if Time.now - @last_moved > @movement_delay and @block.inboundsDown
        @block.pos[0] += 1
        @last_moved = Time.now
      end
    else
      self.boardToDead
      @block = getBlock()
    end  
  end

  def boardToDead
    for row in 0...@board_height
      for col in 0...@board_width
        $dead[row][col] = $board[row][col]
      end
    end
  end

  def deadToBoard
    for row in 0...@board_height
      for col in 0...@board_width
        $board[row][col] = $dead[row][col]
      end
    end
  end

  def blockToBoard()
    array = @block.getArray
    for row in 0...4
      for col in 0...4
        if array[row][col] != 0
          $board[row+@block.pos[0]][col+@block.pos[1]] = array[row][col]
        end
      end
    end
  end

  def draw()
    clearBoard()
    deadToBoard()
    blockToBoard()
    pp $board 
    black = Gosu::Color.argb(0xff000000)
    green = Gosu::Color.argb(0xff00ff00)
    red = Gosu::Color.argb(0xffff0000)
    for i in 0...@board_height
      for j in 0...@board_width
        if $board[i][j] == 0 
          draw_quad(j*@square_length,i*@square_length,black,j*@square_length+@square_length,i*@square_length,black,j*@square_length+@square_length,i*@square_length+@square_length,black,j*@square_length,i*@square_length+@square_length,black)
        end
        if $board[i][j] == 1
          draw_quad(j*@square_length,i*@square_length,green,j*@square_length+@square_length,i*@square_length,green,j*@square_length+@square_length,i*@square_length+@square_length,green,j*@square_length,i*@square_length+@square_length,green)
        end
        if $board[i][j] == 2
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
        if $board[i][j] == 3
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
        if $board[i][j] == 4
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
        if $board[i][j] == 5
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
        if $board[i][j] == 6
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
        if $board[i][j] == 7
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
      end
    end
    @font.draw("#{@score}",10,10,1.0,1.0,1.0,Gosu::Color::WHITE)
  end

  def clearBoard()
    for i in 0...@board_height
      for j in 0...@board_width
        $board[i][j] = 0
      end
    end
  end
end

window = MyWindow.new
window.show
