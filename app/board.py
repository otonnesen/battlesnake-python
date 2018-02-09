class board:

    """
    0 are no snake or chance of snake being there
    1 is no snake but chance of them being there
    2 is there is a snake there
    3 is food
    4 is us
    5 is where we can be
    {
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,3,0,0,0,0,0,5,4,4,4,4,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,1,0,0,0,5,0,0,0,0,0,0,0,0,0,0},
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
        self.board = [[0 for x in range(0, width)] for y in range(0, height)]
        self.width = width
        self.height = height
        self.snake = us
        self.snake_head = us['coords'][0]
        self.Snakes(snakes)

    """
    function to add snakes the board
    """
    def Snakes(self, snakes):
        pass

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
    """
    def check(self):
        moves = ['up', 'down', 'left', 'right']
        not_moves = []
        not_moves.append(self.checkWalls())
        #not_moves.append(self.checkSnakes())
        return list(moves - not_moves)

    """
    tells us where walls are
    """
    def checkWalls(self):
        not_moves = []
        if (self.snake_head[0] <= 1):
            not_moves.append('left')
        elif (self.snake_head[0] >= self.width):
            not_moves.append('up')
        
        if (self.snake_head[1] <= 1):
            not_moves.append('down')
        elif (self.snake_head[1] >= self.height - 1):
            not_moves.append('up')
        
        return not_moves

    def checkSnakes(self):
        pass

