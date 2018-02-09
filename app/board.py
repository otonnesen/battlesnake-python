class board:

    def __init__(self, width, height):
        self.board = [[0 for x in range(0, width)] for y in range(0, height)]
        self.width = width
        self.height = height

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
