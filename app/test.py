from board import board
import json

data = json.load(open('data.json'))

game_board = board(data['width'],data['height'],data['you'],data['snakes'])

# Probably need to store paths as separate entities

def BFS(board, start, depth = 5):
    tmp = []
    stack = []
    stack.insert(0,start)
    out = []
    for count in range(depth):
        tmp = neighbors(stack[-1])
        for i in tmp:
            if i not in out and i not in stack:
                stack.insert(0, i)
        out.append(stack.pop())

    
    return out

# Returns list of coordinates to the left, right, above, and below a given set of coordinates
def neighbors(coords):
    return [{'x':coords['x']-1, 'y':coords['y']},{'x':coords['x']+1, 'y':coords['y']},{'x':coords['x'], 'y':coords['y']-1},{'x':coords['x'], 'y':coords['y']+1}]

# Boolean function
# returns true if coordinates given are OK for the given board,
# false if a snake or wall exists in the same set of coordinates
def spaceOK(board, coord):
    for i in data['snakes']:

        if(data['you']['body']['data'][0] == i['body']['data'][0] and data['you']['length'] > i['length']):
                return true
        for j in i['body']['data']:
            if(coord == j):
                return false
    if(coord['x'] < 0 or coord['x'] > board['width'] - 1 or coord['y'] < 0 or coord['y'] > board['height']):
        return false
            
    return true

print({'x':14,'y':12})
for i in DFS(game_board, {'x':14,'y':12}):
    print(i)
