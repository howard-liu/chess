import chess
import random
from Agents.Agent import Agent

class AntiPawn_Agent(Agent):
  def make_move(self, board):
    # print(board)
    legal_moves = board.legal_moves
    # print(legal_moves)
    # print(dir(legal_moves))
    # count = legal_moves.count
    count = 0
    move_list = []
    for move in legal_moves:
      if str(board.piece_at(move.from_square)).lower() != "p":
        move_list.append(move)
        count += 1
    if count == 0:
      for move in legal_moves:
        move_list.append(move)
        count += 1
    r = random.randint(0,count-1)
    return move_list[r]
