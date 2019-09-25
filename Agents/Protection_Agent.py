import chess
import random
from Agents.Agent import Agent

# Protection: only move if everything is protected

# Let's ignore reward_agent for now, just do a dumb version of protection_agent and we can merge them later

# minimise unprotected pieces

# Protection_Reward_Agent
# TODO: Checkmate > Protect all pieces > Promote to Queen > Capture (with standard score Q>R>B>N>P) > Random move

class Protection_Agent(Agent):
  def unprotected_pieces(self,board):
    # Find all own pieces after move
    # See if all pieces is_attacked_by own side
    unprotected = 0
    for x in range(64):
      # TODO: only white at the moment
      if str(board.piece_at(x)).isupper():
        # print(str(board.piece_at(x)))
        if board.is_attacked_by(True, x) == False:
          # print("unpro")
          unprotected += 1
      # if (self.color == True and str(board.piece_at(x)).isupper() and board.is_attacked_by(True, x) == False):
      #   protected = False
      #   break
      # if (self.color == True and str(board.piece_at(x)).isupper() and board.is_attacked_by(True, x) == False) or (self.color == False and str(board.piece_at(x)).islower() and board.is_attacked_by(False, x) == False):
      #   protected = False
      #   break
    return unprotected
  
  def make_move(self, board):
    legal_moves = board.legal_moves
    count = 0
    selected_move = ""
    move_list = []
    min_unprotected_pieces = 99
    for move in legal_moves:
      next_move_board = board.copy()
      next_move_board.push(move)
      unprotected_pieces = self.unprotected_pieces(next_move_board)
      if unprotected_pieces < min_unprotected_pieces:
        min_unprotected_pieces = unprotected_pieces
        move_list = []
        count = 1
        move_list.append(move)
      elif unprotected_pieces == min_unprotected_pieces:
        move_list.append(move)
        count += 1
    # print("min unpro")
    # print(min_unprotected_pieces)
    if count == 0:
      # print("No safe moves")
      for move in legal_moves:
        selected_move = move
        break
    else:
      # print("Safe moves")
      # print(move_list)
      r = random.randint(0,count-1)
      selected_move = move_list[r]
    return selected_move