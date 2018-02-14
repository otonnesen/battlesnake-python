from board import board
import json

data = json.load(open('data.json'))

game_board = board(data)

print(game_board)
coord1 = {'x':4,'y':5}
coord2 = {'x':7,'y':12}
coord3 = {'x':13,'y':3}
coord4 = {'x':0,'y':1}
print(coord1)
print(coord2)
print(coord3)
print(coord4)
game_board.plot(coord1, 1)
game_board.plot(coord2, 1)
game_board.plot(coord3, 1)
game_board.plot(coord4, 1)
print(game_board)
