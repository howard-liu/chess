import chess
from Board import Board
from Agents.Random_Agent import Random_Agent
from Agents.Human_Agent import Human_Agent
from Agents.Pawn_Agent import Pawn_Agent
from Agents.AntiPawn_Agent import AntiPawn_Agent
from Agents.Reward_Agent import Reward_Agent
from Agents.NSReward_Agent import NSReward_Agent
from Agents.Protection_Agent import Protection_Agent


# TODO:
# Protection: only move if everything is protected
# Endgame: when there is only king left for other player, march king towards other king (or something)
# Centre control: move towards centre at the earlygame
# Push pawns: To test pawn promotion into queen to enforce in Reward_Agent etc

for x in range(1000):
  board = Board()
  # White Agent
  white_player = Reward_Agent(board.board, True)
  # Black Agent
  black_player = Reward_Agent(board.board, False)
  # Initial Board
  print("Starting board")
  board.print()
  # Let's start with max game length 500 moves
  for x in range(1,500):
    # White turn
    print(board.turn + "'s turn")
    move = white_player.make_move(board.board)
    move_selected = chess.Move.from_uci(str(move))
    # print(move_selected)
    board.take_turn(move)
    if (board.check_result() == True):
      board.print()
      break
    board.print()

    # Black turn
    print(board.turn + "'s turn")
    move = black_player.make_move(board.board)
    board.take_turn(move)
    if (board.check_result() == True):
      board.print()
      break
    board.print()
