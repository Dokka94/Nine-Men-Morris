class Pieces:
    def __init__(self, x, y, place, color):
        self.x = x
        self.y = y
        self.place = place
        self.color = color
        self.mill = False

    def move(self, newplace):
        # TODO
        pass

    def setMill(self, b):
        self.mill = b

    def setColor(self, color):
        self.color = color
