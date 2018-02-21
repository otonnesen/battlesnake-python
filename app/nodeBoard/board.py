class board:

    # Board Data Structure:
    # {
    #   'food' : bool
    #      True        if food
    #      False       if no food
    #   'snake' : str
    #      'body'      if enemy snake body
    #      'head'      if enemy snake head
    #      'bodyYou'   if your body
    #      'headYou'   if your head
    #   'value': int
    #       sum of values defined below under 'Board Constants'
    # }

    # TODO: Implement 'value' to board data
    # Currently only 'snake' and 'food' data are modified by populateBoard
    
    # Board Constants

    FOOD = -3
    KILLABLE_SNAKE = -2
    EMPTY_TILE = 0
    DANGEROUS_TILE = 4
    ENEMY_SNAKE = 5



    def __init__(self, data):
        self.food = data['food']['data']
        self.width = data['width']
        self.height = data['height']
        self.board = [[{'food':False,'snake':None,'value':0} for y in range(self.height)] for x in range(self.width)]
        self.you = data['you']
        self.snakes = data['snakes']['data']
        for i in self.snakes:
            if(i['id'] == self.you['id']):
                self.snakes.remove(i)

    # Full board
    # Node, coordList is optional, and not called when printing the board normally
    # It allows a list of coordinates to be input to see their path on the board for testing purposes
    def __str__(self, coordList = []):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[x][y]['snake'] == None and self.board[x][y]['food'] == False):
                    tmp.append('___')
                elif(self.board[x][y]['snake'] == 'body'):
                    tmp.append('_B_')
                elif(self.board[x][y]['snake'] == 'head'):
                    tmp.append('_H_')
                elif(self.board[x][y]['snake'] == 'bodyYou'):
                    tmp.append('_y_')
                elif(self.board[x][y]['snake'] == 'headYou'):
                    tmp.append('_Y_')
                elif(self.board[x][y]['food']):
                    tmp.append('_F_')

###########################################################################
#                             Optional
#                            Path Testing

                for i in coordList:
                    if(i['x'] == x and i['y'] == y):
                        tmp[x] = '=^='
                if(coordList[0]['x'] == x and coordList[0]['y'] == y):
                    tmp[x] = 'BEG'
                if(coordList[-1]['x'] == x and coordList[-1]['y'] == y):
                    tmp[x] = 'END'

###########################################################################

            s.append(''.join(tmp)+'\n')
            tmp = []

        return ''.join(s)

    # Only snake board
    def getSnakeBoard(self):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[x][y]['snake'] == None):
                    tmp.append(0)
                elif(self.board[x][y]['snake'] == 'body'):
                    tmp.append(1)
                elif(self.board[x][y]['snake'] == 'head'):
                    tmp.append(2)
                elif(self.board[x][y]['snake'] == 'bodyYou'):
                    tmp.append(3)
                elif(self.board[x][y]['snake'] == 'headYou'):
                    tmp.append(4)
            s.append(tmp)
            tmp = []
        return s

    # Only food board
    def getFoodBoard(self):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[x][y]['food']):
                    tmp.append(1)
                else:
                    tmp.append(0)
            s.append(tmp)
            tmp = []
        return s

    # Prints out above function
    def snakeBoardString(self):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[x][y]['snake'] == None):
                    tmp.append('___')
                elif(self.board[x][y]['snake'] == 'body'):
                    tmp.append('_B_')
                elif(self.board[x][y]['snake'] == 'head'):
                    tmp.append('_H_')
                elif(self.board[x][y]['snake'] == 'bodyYou'):
                    tmp.append('_y_')
                elif(self.board[x][y]['snake'] == 'headYou'):
                    tmp.append('_Y_')
            s.append(''.join(tmp)+'\n')
            tmp = []
        return ''.join(s)

    # Prints out above function
    def foodBoardString(self):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                if(self.board[x][y]['food']):
                    tmp.append('_F_')
                else:
                    tmp.append('___')
            s.append(''.join(tmp)+'\n')
            tmp = []
        return ''.join(s)
    # Fills the board with empty dictionaries
    def plot(self, coords, field, value):
        if(coords['x'] < self.width and coords['x'] >= 0 and coords['y'] < self.height and coords['y'] >= 0):
            self.board[coords['x']][coords['y']][field] = value

    # Returns the value of the 'field' field of a set of coordinates' dictionary
    def getData(self, coords, field):
        return self.board[coords['x']][coords['y']][field]

    # Sets the value of a set of coordinates' 'snake' field
    def setSnake(self, coords, value):
        self.plot(coords, 'snake', value)
    
    # Sets the value of a set of coordinates' 'food' field
    def setFood(self, coords, value):
        self.plot(coords, 'food', value)

    # Sets food/snake values for the full board
    def populateBoard(self):
        for snake in self.snakes:
            self.setSnake(snake['body']['data'][0], 'head')
            for i in snake['body']['data'][1:]:
                self.setSnake(i, 'body')
        self.setSnake(self.you['body']['data'][0], 'headYou')
        for i in self.you['body']['data'][1:]:
            self.setSnake(i, 'bodyYou')
        for i in self.food:
            self.setFood(i, True)
