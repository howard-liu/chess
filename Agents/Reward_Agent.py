import chess
import random
from Agents.Agent import Agent

# TODO: Checkmate > Promote to Queen > Capture (with standard score Q>R>B>N>P) > --Check-- > Random move

# Finding: implementing check as a priority over random move, caused agent to draw with random move

# Only draws w random when stalemates: maybe needs to evaluate when ahead try not to stalemate

class Reward_Agent(Agent):
  def make_move(self, board):
    legal_moves = board.legal_moves
    count = 0
    capture_count = 0
    captures = []
    checks = []
    others = []
    selected_move = ""
    for move in legal_moves:
      next_move_board = board.copy()
      next_move_board.push(move)
      if next_move_board.is_checkmate():
        # print("MATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATEMATE")
        selected_move = move
        break
      elif ("1" in str(move) or "8" in str(move)) and str(board.piece_at(move.from_square)).lower() == "p":
        # print("PROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTEPROMOTE")
        selected_move = move
        break
      elif board.is_capture(move) == True:
        print("CAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURECAPTURE")
        captures.append(move)
      # Checks
      # elif captures == [] and next_move_board.is_check():
      #   print("CHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECKCHECK")
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
