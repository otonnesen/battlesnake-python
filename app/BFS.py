def neighbors(coords):
    return [[coords[0]-1,coords[1]], [coords[0]+1,coords[1]], [coords[0],coords[1]-1], [coords[0],coords[1]+1]]

def BFS(start, goal, board):
    visited = [start]
    q = [start]
    path = []
    findPath = {}
    while q:
        c = q.pop()
        if(not board.spaceOK(c)):
            continue
        if c == goal:
            path.append(c)
            break
        path.append(c)
        for i in neighbors(c):
            if i not in visited:
                findPath[str(i)] = c
                q.insert(0,i)
                visited.append(i)

    out = []
    c = path[-1]
    while c != start:
        out.insert(0,c)
        c = findPath[str(c)]

    return out
