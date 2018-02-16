from board import board
import json
import time

test = []
# Checks to see if there exists at least one path of length 'depth' from 'start' to any safe tile
# TODO: Implement safety check on each tile (How many turns away is an unavoidable snake?)
def findPath(board, start, depth = 5):
    for i in neighbors(start):
        if(findPathRecur(board, i, depth - 1) and spaceOK(game_board, i)):
            test.append(i)
            test.append(start)
            test.reverse()
            return i
    return False

def findPathRecur(board, start, depth):
    if(depth == 0):
        if(spaceOK(board, start)):
            return True
        return False

    for i in neighbors(start):
        if(findPathRecur(board, i, depth -1) and spaceOK(board, i)):
            test.append(i)
            return i



def neighbors(coords):
    return [{'x':coords['x']-1, 'y':coords['y']},{'x':coords['x']+1, 'y':coords['y']},{'x':coords['x'], 'y':coords['y']-1},{'x':coords['x'], 'y':coords['y']+1}]

# Maybe convert to using board 'value' data 
# instead of raw input data
def spaceOK(board, coords):
    for i in board.snakes:
        if(coords == i['body']['data'][0] and board.you['length'] > i['length']): # Realized this doesn't work since we don't know the current position of the head
            return True
        for j in i['body']['data']:
            if(coords == j):
                return False
    if(coords['x'] < 0 or coords['x'] > board.width - 1 or coords['y'] < 0 or coords['y'] > board.height):
        return False

    return True


# TESTING


dataFile = 'data3.json'
data = json.load(open(dataFile))
game_board = board(data)
game_board.populateBoard()
startingPoint = {'x':5,'y':7}

# findPath(game_board, coord1, 15)
# print(game_board.__str__(test))

# Timing pathFind with different depths

print("Datafile used: "+dataFile+"\nStarting point: ("+str(startingPoint['x'])+","+str(startingPoint['y'])+")")
for i in range(1,25):
    start = time.time()
    findPath(game_board, startingPoint, i)
    end = time.time()
    print("Depth: "+str(i)+", time: "+str(end-start)+"s")

# Initial findings: Maximum reasonalbe depth (<200ms) is 12 to 13
# Probably big enough and optimization not needed (unless we end up implementing
# a directed pathfinding algorithm such as Dijkstra or A*, at which point this algorithm
# becomes essentially useless)
