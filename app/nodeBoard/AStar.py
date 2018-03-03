from point import point
import heapq

# Returns Euclidean distance between two points
# Note: does not check if points are safe or valid
def distance(start, end):
    return ((start.x-end.x)**2+(start.y-end.y)**2)**0.5

# Returns 'up', 'down', 'left', or 'right'
# based on where end is relative to start
def direction(start, end):
    dx = start.x - end.x
    dy = start.y - end.y
    if(abs(dx) > abs(dy)):
        if(dx > 0):
            return 'left'
        else:
            return 'right'
    else:
        if(dy > 0):
            return 'up'
        else:
            return 'down'

# Function that minimizes function
# f(x) = g(x) + h(x)
# Where n(x) is the nodal distance between x and start
# and d(x) is the Euclidean distance between x and start
def AStar(start, goal):
    # Priority Queue
    evaluated = []

    # Priority Queue
    toEval = []

    heapq.heappush(toEval, (0, start))

    # Dictionary of nodes from which each element can be most easily reached
    cameFrom = {}

    # Dictionary of total smallest f(x) to each node
    dScore = {}

    nScore[start] = 0

    dScore[start] = distance(start, goal)

    while evaluated:
        current = heapq.heappop(toEval)
        if(current[1] == goal):
            return # the path from start to goal
    
        heapq.heappush(evaluated, (
