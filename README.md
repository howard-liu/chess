# Chess

## Inspiration

I've been enjoying playing chess and am amazed at AI's dominance in chess. This project is inspired by [this video](https://www.youtube.com/watch?v=DpXy041BIlA) by Tom7 (suckerpinch), I highly recommend it to anyone who enjoys chess, AI, tournaments, battles or even colourful graphs.

## What I have used

This project is written in python runs off of the amazing [python-chess](https://pypi.org/project/python-chess/), so I didn't have to deal with programming in all the finicky edge cases of chess like castling and en passant. Other than that, this library has built in a great deal of functions to make programming AIs significantly easier.

## What is the project
So far, this project is a command line chess game that is usually played between AIs. I have written different agents who have different strategies and priorities.
So far I have created:
- Random Agent: randomly chooses a legal move
- Pawn Agent: prioritises pawn moves first, causes it to push pawns aggressively
- AntiPawn Agent: opposite of Pawn Agent, prioritises non-pawn moves first (hates knights)
- Reward Agent: has basic ideas of chess - Checkmate > Promote to Queen > Capture (with standard score Q>R>B>N>P) > Random move
- NSReward Agent (No Stalemate): Same as Reward Agent, but checks for stalemate before moving (if ahead in material)
- Protection Agent: Minimises unprotected pieces (does not care about enemy attacks)
- Human Agent: you can play too!

## Interesting Insights

Pawn > AntiPawn. I thought, before I saw it perform, that AntiPawn would align with chess principles of development and allow for some aggressive starts. Then I found of that it only moves (and suicides) its knights, then opens the pawns. Being two knights down is what makes AntiPawn perform worse than Random.

Reward Agent beats Random-based Agents around 95% of the time (needs actual statistical backup), with the other times being draws due to accidental stalemate (usually while being miles ahead in material) (eventually Random Agent should win one because it has a chance of making all the right moves). This is what inspired the conception of NSReward Agent. No Stalemate Reward Agent's goal is to capitalise on weak opponents and checkmate them instead of accidentally drawing. This means that it checks if the move it will make will stalemate the game. However, if you are behind, sometimes a draw is the best you can hope for, so I implemented a material balance check to see who is ahead. If NSReward Agent is ahead, it will go for the kill. 

Rewards/NSReward Agent behaves significantly worse when it prioritises checks before random moves. Under closer inspection, this makes sense as in the endgame, constantly checking the opponent while ahead nearly always leads to a draw, whereas random moves allow pawns to be pushed, and dumb luck to prevail

Once I implemented the check for one move checkmates, I enjoyed when the AI found some interesting and sometimes elegant checkmates. Some of which I have saved and maybe will share later on

## To Do:
### Interesting Agent Ideas
- Defence: Protection and the ability to see what squares the enemy controls and respond to that
- Endgame: when there is only king left for other player, march king towards other king (or something)
- Centre control: move towards centre at the earlygame
- Push pawns: To test pawn promotion into queen to enforce in Reward Agent etc
- Opening database: Download lichess.org database and get Agent to play from that
- Minimax: "Normal" chess AI with depth search, minimax, alpha-beta pruning and all that
- SUPER AGENT: Combine the best of all of parts to build the best Agent I can
### Tournament
When there are enough Agents, I want to have them battle it out over hundreds of games to see exactly how they perform against each other
### vs Human
Test eventual stronger Agents vs human players of different skill levels (I believe that without depth searching, an Agent should be able to be at least 1000 ELO on lichess.org)
