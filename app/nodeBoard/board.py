class board:

    def __init__(self, data):
        self.food = data['food']['data']
        self.width = data['width']
        self.height = data['height']
        self.board = [[{'food':False,'snake':None} for y in range(self.height)] for x in range(self.width)]
        self.you = data['you']
        self.snakes = data['snakes']['data']
        for i in self.snakes:
            if(i['id'] == self.you['id']):
                self.snakes.remove(i)

    # Full board
    def __str__(self):
        s = []
        tmp = []
        for y in range(self.height):
            for x in range(self.width):
                tmp.append(self.board[x][y])
            s.append(str(tmp)+'\n')
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
                    tmp.append('_')
                elif(self.board[x][y]['snake'] == 'body'):
                    tmp.append('B')
                elif(self.board[x][y]['snake'] == 'head'):
                    tmp.append('H')
                elif(self.board[x][y]['snake'] == 'bodyYou'):
                    tmp.append('y')
                elif(self.board[x][y]['snake'] == 'headYou'):
                    tmp.append('Y')
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
                    tmp.append('F')
                else:
                    tmp.append('_')
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
