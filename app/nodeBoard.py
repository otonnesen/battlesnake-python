from LinkedList import LinkedList
class board:

    def __init__(self, data):
        self.width = data['width']
        self.height = data['height']
        self.board = [LinkedList() for x in range(self.width)]
        for x in self.board:
            for y in range(self.height):
                x.append(0)
        self.you = data['you']
        self.snakes = data['snakes']

    def __str__(self):
        s = []
        tmp = []
        for i in range(self.width):
            for j in range(self.height):
                tmp.append(self.board[j].index(i))
            s.append(str(tmp)+'\n')
            tmp = []
        return ''.join(s)

    def plot(self, coords, value):
        if(coords['x'] < self.width and coords['x'] >= 0 and coords['y'] < self.height and coords['y'] >= 0):
            self.board[coords['x']].set(coords['y'], value)
