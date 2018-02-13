from board import board
import json

data = json.load(open('data.json'))

game_board = board(data['width'],data['height'],data['you'],data['snakes'])

def pathFind(board, start, depth = 5):
    current = start
    tmp = []
    stack = []
    for n in neighbors(start):
        for i in range(depth):
            for j in neighbors(current):
                if(spaceOK(board, j)):
                    tmp.append(j)
                    current = j
                    break
        stack.append(tmp)
        tmp = []
    return stack

# Returns list of coordinates to the left, right, above, and below a given set of coordinates
def neighbors(coords):
    return [{'x':coords['x']-1, 'y':coords['y']},{'x':coords['x']+1, 'y':coords['y']},{'x':coords['x'], 'y':coords['y']-1},{'x':coords['x'], 'y':coords['y']+1}]

# Boolean function
# returns True if coordinates given are OK for the given board,
# False if a snake or wall exists in the same set of coordinates
def spaceOK(board, coord):
    for i in data['snakes']['data']:

        if(data['you']['body']['data'][0] == i['body']['data'][0] and data['you']['length'] > i['length']):
                return True
        for j in i['body']['data']:
            if(coord == j):
                return False
    if(coord['x'] < 0 or coord['x'] > board.width - 1 or coord['y'] < 0 or coord['y'] > board.height):
        return False
            
    return True

print({'x':14,'y':12})
for i in pathFind(game_board, {'x':14,'y':12}):
    print(i)
