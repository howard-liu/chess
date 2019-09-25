import chess

class Agent:
  def __init__(self, board, color):
    self.board = board
    self.color = color

  def update_board(self, board):
    self.board = board


