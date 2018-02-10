class board ():

    """
    -3 there is food
    -2 there is a bot we can kill
    0 there is a open space no snake will be on the next turn
    4 a snake may be there on the next turn that will kill us
    5 a snake body part
    we add values on a square and take the lowest square lower is better
    case 1: no snakes around us then lowest option would be 4 we would take it
        {00040000}
        {00454000}
        {00050000}
        {00000000}
    case 2: food on a piece we can get to so 4 + (-3) we would go to that piece
        {00040000}
        {00451000}
        {00050000}
        {00000000}
    case 3: snake body on a part that we could go to next so 4 + 9 
            (note five is both us and the other snake)
        {00045400}
        {00459000}
        {00050000}
        {00000000}
    case 4: snake may move there and is the same size or bigger next turn so 4 + 4
        {00040000}
        {00458555}
        {00050000}
        {00000000}
    case 5: snake is smaller than us and may move there (we want to kill it)
            so 4 + (-2)
        {00040000}
        {00452550}
        {00050000}
        {00050000}
    {
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,3,0,0,0,0,0,1,4,4,4,4,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
    }
    """
    def __init__(self, width, height, us, snakes): # model needs reviewing
        self.board = [[0 for y in range(0, height)] for x in range(0, width)]
        self.width = width
        self.height = height
        self.snake = us
        self.snake_head = us['body']['data'][0]
        self.other_snakes = snakes

    """
    function to add snakes the board
    """
    def Snakes(self, snakes): # needs redoing
        for snake in snakes['data']:
            # if the snake will kill us on collision put a one where it can be
            if snake['length'] >= self.snake['length']:
                self.plot(snake['body']['data'][0]['x'] + 1, snake['body']['data'][0]['y'], 3)
                self.plot(snake['body']['data'][0]['x'] - 1, snake['body']['data'][0]['y'], 3)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] + 1, 3)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] - 1, 3)
            else: # the snake will die on collision
                self.plot(snake['body']['data'][0]['x'] + 1, snake['body']['data'][0]['y'], -2)
                self.plot(snake['body']['data'][0]['x'] - 1, snake['body']['data'][0]['y'], -2)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] + 1, -2)
                self.plot(snake['body']['data'][0]['x'], snake['body']['data'][0]['y'] - 1, -2)
            
            for coord in snake['body']['data']:
                self.plot(coord['x'], coord['y'], 4)

    """
    adds our own snake on the map
    """
    def plotSelf(self): # this might not be needed
        for bodypart in self.snake['body']['data']:
            self.plot(bodypart['x'], bodypart['y'], 5)
        

    """
    function to clear the board at the end of the turn
    """
    def clear(self): # probably not needed becuase every request we remake the board
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
    def check(self): # we can keep adding to this
        moves = ['up', 'down', 'left', 'right']
        not_moves = []
        not_moves = not_moves + self.checkWalls()
        not_moves = not_moves + self.checkSnakes()
        #not_moves.append(self.checkSnakes())
        return list(set(moves).difference(not_moves))

    """
    tells us where walls are
    """
    def checkWalls(self): # Done
        not_moves = []
        if (self.snake_head['x'] == 0):
            not_moves.append('left')
        elif (self.snake_head['x'] == self.width-1):
            not_moves.append('right')
        
        if (self.snake_head['y'] == 0):
            not_moves.append('up')
        elif (self.snake_head['y'] == self.height-1):
            not_moves.append('down')
        
        return not_moves

    """
    checks for collisions with snakes
    """
    def checkSnakes(self): # needs to be redone
        not_moves = []
        """
        if were not going to look out of bounds
            look one above, below, or beside our snakes head
            and if that is a dangerous block dont go there
        """
        if self.snake_head['x']+1 < self.width: 
            right = self.board[self.snake_head['x'] + 1][self.snake_head['y']]
            if right == 3 or right == 5:
                not_moves.append('right')

        if self.snake_head['x']-1 >= 0:
            left = self.board[self.snake_head['x'] - 1][self.snake_head['y']]
            if left == 3 or left == 5:
                not_moves.append('left')
        
        if self.snake_head['y']+1 < self.height:
            down = self.board[self.snake_head['x']][self.snake_head['y'] + 1]
            if down == 3 or down == 5:
                not_moves.append('down')

        if self.snake_head['y']-1 >= 0:
            up = self.board[self.snake_head['x']][self.snake_head['y'] - 1]
            if up == 3 or up == 5:
                not_moves.append('up')

        return not_moves
        


    def plot(self, x, y, num): # Done
        if (x < self.width and x >= 0) and (y < self.height and y >= 0):
            self.board[x][y] = num

    def run(self):
        self.Snakes(self.other_snakes)
        self.plotSelf()