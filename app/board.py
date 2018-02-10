class board ():

    """
    0 are no snake or chance of snake being there
    1 is no snake but chance of them being there and they will kill us
    2 is no snake but chance of them being there wont kill us
    3 is there is a snake there
    4 is food
    5 is us
    6 is where we can be
    {
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,3,0,0,0,0,0,6,5,5,5,5,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,1,0,0,0,6,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,2,0,0,0,0,0,0,3,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
    }
    """
    def __init__(self, width, height, us, snakes):
        self.board = [[0 for y in range(0, height)] for x in range(0, width)]
        self.width = width
        self.height = height
        self.snake = us
        self.snake_head = us['body']['data'][0]
        self.other_snakes = snakes

    """
    function to add snakes the board
    """
    def Snakes(self, snakes):
        for snake in snakes['data']:
            # if the snake will kill us on collision put a one where it can be
            if snake['length'] >= self.snake['length']:
                self.plot(snake['body']['data'][0]['x'] + 1, snake['body']['data'][0]['y'], 1)
                self.plot(snake['body']['data'][0]['x'] - 1, snake['body']['data'][0]['y'], 1)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] + 1, 1)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] - 1, 1)
            else: # the snake will die on collision
                self.plot(snake['body']['data'][0]['x'] + 1, snake['body']['data'][0]['y'], 2)
                self.plot(snake['body']['data'][0]['x'] - 1, snake['body']['data'][0]['y'], 2)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] + 1, 2)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] - 1, 2)
            
            for coord in snake['body']['data']:
                self.plot(coord['x'], coord['y'], 3)

    """
    function to clear the board at the end of the turn
    """
    def clear(self):
        pass
    
    """
    Function adds food to the board
    """
    def food(self, food):
        pass

    """
    Basically whats going to kill us? dont do that
    returns: a list of moves that wont kill us
    """
    def check(self):
        moves = ['up', 'down', 'left', 'right']
        not_moves = []
        not_moves = not_moves + self.checkWalls()
        #not_moves.append(self.checkSnakes())
        return list(set(moves).difference(not_moves))

    """
    tells us where walls are
    """
    def checkWalls(self):
        not_moves = []
        if (self.snake_head['x'] <= 1):
            not_moves.append('left')
        elif (self.snake_head['x'] >= self.width):
            not_moves.append('right')
        
        if (self.snake_head['y'] <= 0):
            not_moves.append('up')
        elif (self.snake_head['y'] >= self.height):
            not_moves.append('down')
        
        return not_moves

    def checkSnakes(self):
        pass

    def plot(self, x, y, num):
        if (x < self.width and x >= 0) and (y < self.height and y >= 0):
            self.board[x][y] = num
