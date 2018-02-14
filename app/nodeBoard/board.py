from LinkedList import LinkedList
class board:

    def __init__(self, data):
        self.food = data['food']
        self.width = data['width']
        self.height = data['height']
        self.board = [[{'food':False,'snake':False} for y in range(self.height)] for x in range(self.width)]
        self.you = data['you']
        self.snakes = data['snakes']

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
                if(self.board[x][y]['snake']):
                    tmp.append(1)
                else:
                    tmp.append(0)
            s.append(str(tmp)+'\n')
            tmp = []
        return ''.join(s)

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
            s.append(str(tmp)+'\n')
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
        for snake in self.snakes['data']:
            for i in snake['body']['data']:
                self.setSnake(i, True)
        for i in self.food['data']:
            self.setFood(i, True)
