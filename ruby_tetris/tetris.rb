#!/usr/bin/env ruby

require 'pp'
require 'gosu'

class MyWindow < Gosu::Window
  def initialize
    super(800,800,false)
    self.caption = "Tetris"
    @font = Gosu::Font.new(self,"Arial",14)
    @board_height = 20
    @board_width = 10
    for i in 0..@board_height
      row = []
      for j in 0..@board_width
        row.push(0)
      end
      @board.push(row)
    end
    @movement_delay = 0.05
    @last_moved = Time.now
    @score = 0
  end

  def update()
    if button_down? Gosu::KbLeft
      @block.pos[1] += 1
    end
    if button_down? Gosu::KbRight
      @block.pos[1] -= 1
    end
    if button_down? Gosu::KbUp
      @block.rotate
    end
    if button_down? Gosu::KbDown
      @block.down
    end
    if button_down? Gosu::KbEscape
      close
    end
    if Time.now - @last_moved > @movement_delay
      @block.pos[1] += 1
    end
  end

  def draw()
    clearBoard()
    @snake.each do |point| 
      @board[point[0]][point[1]] = 1
    end
    @board[@bit[0]][@bit[1]] = 2
    black = Gosu::Color.argb(0xff000000)
    green = Gosu::Color.argb(0xff00ff00)
    red = Gosu::Color.argb(0xffff0000)
    for i in 0..@board_height
      for j in 0..@board_width
        if @board[i][j] == 0
          draw_quad(j*@square_length,i*@square_length,black,j*@square_length+@square_length,i*@square_length,black,j*@square_length+@square_length,i*@square_length+@square_length,black,j*@square_length,i*@square_length+@square_length,black)
        end
        if @board[i][j] == 1
          draw_quad(j*@square_length,i*@square_length,green,j*@square_length+@square_length,i*@square_length,green,j*@square_length+@square_length,i*@square_length+@square_length,green,j*@square_length,i*@square_length+@square_length,green)
        end
        if @board[i][j] == 2
          draw_quad(j*@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length,red,j*@square_length+@square_length,i*@square_length+@square_length,red,j*@square_length,i*@square_length+@square_length,red)
        end
      end
    end
    @font.draw("#{@score}",10,10,1.0,1.0,1.0,Gosu::Color::WHITE)
  end

  def clearBoard()
    for i in 0..@board_length
      for j in 0..@board_length
        @board[i][j] = 0
      end
    end
  end
end

window = MyWindow.new
window.show
