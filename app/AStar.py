from point import point
import heapq

# Returns Euclidean distance between two points
# Note: does not check if points are safe or valid
def eucDistance(start, end):
    return ((start.x-end.x)**2+(start.y-end.y)**2)**0.5

def manDistance(start, end):
    dx = start.x - end.ex
    dy = start.y - end.y
    return dx + dy

def heuristic(start, end):
        return eucDistance(start, end) + manDistance(start, end)

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

def neighbors(coords):
    return [point(coords.x-1,coords.y),point(coords.x+1,coords.y),point(point.x,point.y-1),point(point.x,point.y+1)]

# Function that minimizes function
# f(x) = g(x) + h(x)
# Where n(x) is the nodal distance between x and start
# and d(x) is the Euclidean distance between x and start
def AStar(start, goal):
    # Priority Queue
    closedSet = []

    # Priority Queue
    openSet = []

    heapq.heappush(toEval, (0, start))

    # Dictionary of nodes from which each element can be most easily reached
    cameFrom = {}

    # Dictionary of total smallest f(x) to each node
    gScore = {}

    gScore[start] = 0

    fScore = {}

    fScore[start] = heuristic(start, goal)

    while openSet:
        current = heapq.heappop(openSet)
        if(current[1] == goal):
            return cameFrom

        openSet.remove(current)
        closedSet.append(current)

        for n in neighbors(current):
            if n in closedSet:
                continue
            else:
                openSet.add(n)
            tentative_gScore = gScore[current] + 1
            if(tentative_gScore > gScore[neighbor]):
                continue # Not improved path

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal)

    return False
