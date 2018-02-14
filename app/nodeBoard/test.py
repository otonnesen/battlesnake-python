from board import board
import json
import time

start = time.time()

data = json.load(open('data2.json'))
game_board = board(data)
game_board.populateBoard()

end = time.time()

print(game_board.snakeBoardString())
print(game_board.foodBoardString())

print('Set up board in '+str(end-start)+' seconds')
