from board import board
import json

data = json.load(open('data2.json'))

game_board = board(data)

game_board.populateBoard()

print('Food Board')
print(game_board.getFoodBoard())
print('\nSnake Board')
print(game_board.getSnakeBoard())
