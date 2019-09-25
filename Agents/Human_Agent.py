import chess
from Agents.Agent import Agent

class Human_Agent(Agent):
  def make_move(self, board):
    accepted_move = False
    san = ""
    # Currently has no checks for valid moves or not
    # while accepted_move == False:
    san = input("Enter move to continue, eg: Nf5\n")
      # if san in board.legal_moves:
      #   accepted_move = True
    print(san)
    return san
