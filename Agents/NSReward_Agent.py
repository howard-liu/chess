import chess
import random
from Agents.Agent import Agent

# Checkmate > Promote to Queen > Capture (with standard score Q>R>B>N>P) > --Check-- > Random move

# Finding: implementing check as a priority over random move, caused agent to draw with random move
# Checking as a priority causes a lot of unnecessary moves (could be used eg pushing pawns)

# Only draws w random when stalemates: maybe needs to evaluate when ahead try not to stalemate
# This is no stalemate version of Reward Agent

class NSReward_Agent(Agent):
  def make_move(self, board):
    legal_moves = board.legal_moves
    count = 0
    captures = []
    checks = []
    others = []
    selected_move = ""
    # print("material:")
    # print(self.material_difference(board))
    for move in legal_moves:
      next_move_board = board.copy()
      next_move_board.push(move)
      # print(next_move_board.turn)
      if next_move_board.is_checkmate():
        # print("MATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATE")
        selected_move = move
        break
      # Avoid stalemate when ahead in material
      elif next_move_board.is_stalemate() and self.material_difference(board) > 0:
        # print("STALEMATEAVOIDEDSTALEMATEAVOIDEDSTALEMATEAVOIDEDSTALEMATEAVOIDEDSTALEMATEAVOIDED")
        # TODO: delete move so cannot be accessed my random
        pass
      elif ("1" in str(move) or "8" in str(move)) and str(board.piece_at(move.from_square)).lower() == "p":
        print("PROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTE")
        print(move)
        selected_move = move
        break
      elif board.is_capture(move) == True:
        # print("CAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURE")
        captures.append(move)
      # Checks (removed)
      # elif captures == [] and next_move_board.is_check():
      #   # print("CHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECK")
      #   checks.append(move)
      else:
        # print("testerino")
        others.append(move)
        count += 1
    
    if captures != []:
      # print('testo')
      for capture in captures:
        if str(board.piece_at(move.to_square)).lower() == "q":
          selected_move = capture
        elif str(board.piece_at(move.to_square)).lower() == "r":
          selected_move = capture
        elif str(board.piece_at(move.to_square)).lower() == "b":
          selected_move = capture
        elif str(board.piece_at(move.to_square)).lower() == "n":
          selected_move = capture
        else:
          selected_move = capture
    # elif checks != []:
    #   print('testo2')
    #   selected_move = checks.pop()
    elif selected_move == "":
      # print("hello")
      r = random.randint(0,count-1)
      selected_move = others[r]
    
    # print(str(selected_move))
    return selected_move
  
  def material_difference(self, board):
    total = 0
    for x in range(64):
      # print(board.piece_at(x))
      val = 0
      if str(board.piece_at(x)).lower() == "p":
        val = 1
      elif str(board.piece_at(x)).lower() == "k":
        val = 3
      elif str(board.piece_at(x)).lower() == "b":
        val = 3
      elif str(board.piece_at(x)).lower() == "r":
        val = 5
      elif str(board.piece_at(x)).lower() == "q":
        val = 9
      if str(board.piece_at(x)).islower():
        val *= -1
      total += val
    if self.color == False:
      total *= -1
    return total
      
