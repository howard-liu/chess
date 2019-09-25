import chess

class Board:
  def __init__(self):
    self.board = chess.Board()
    self.turn = 'white'

  def print(self):
    print(self.board)

  def print_legal_moves(self):
    print(self.board.legal_moves)

  def take_turn(self, move):
    if len(str(move)) == 4 or len(str(move)) == 5:
      move_selected = chess.Move.from_uci(str(move))
      self.board.push(move_selected)
    elif len(str(move)) == 2 or len(str(move)) == 3:
      self.board.push_san(move)
    else:
      print("move reading error: oops...")
    # Check for checkmate (declare winner)
    # Check stalemate (declare draw)
    if self.board.is_game_over == True:
      print(self.board.result)
      return "gameover"

    if self.turn is 'white':
      self.turn = 'black'
    else:
      self.turn = 'white'
    print("Turn: " + str(self.board.fullmove_number))
    

  def check_result(self):
    # print("is game over?:")
    # print(self.board.is_game_over())
    if self.board.is_game_over() == True:
      print(self.board.result())
      return True
    else:
      return False
    

  