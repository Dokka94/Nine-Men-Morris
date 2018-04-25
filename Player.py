import Pieces


class Player:
    def __init__(self, color, starter, board):
        # TODO
        self.color = color
        self.starter = starter
        self.board = board
        # self.oppenent = self.setOpponent(opponent)
        self.pieces = []
        self.state = 0
        self.number_of_pieces = 0
        self.take = False
        self.place_from = False
        self.chosen = 0
        self.next = False

    def setOpponent(self, opponent):
        # TODO
        self.opponent = opponent

    # in this function, based on the game's state
    # it will calls 3 different function step1,step2,step3
    def next_step(self, x, y, place):
        # TODO
        pass

    def step1(self, x, y, newplace):
        # TODO
        pass

    def step2(self, x, y, newplace):
        # TODO
        pass

    def step3(self, x, y, newplace):
        # TODO
        pass

    def step_from(self, x, y, newplace):
        # TODO
        pass

    # if a piece placed in the place,
    #  will it be a mill?
    # calls the mills(a,b,c) function

    def willbe_mill(self, place):
        # TODO
        return False
    # check if the given three numbers
    # perform a mill

    def mills(self, a, b, c):
        # TODO
        return False

    def moveablePieces(self):
        # TODO
        return [Pieces]

    def removeablePieces(self):
        # TODO
        return [Pieces]

    def neighbours(self):
        # TODO
        return [Pieces]

    def lose(self):
        # TODO
        pass

    def removeable(self, place):
        # TODO
        return False

    def reserved(self, place):
        # TODO
        return False

    def setNext(self, b):
        self.next = b

    def updateMills(self):
        # TODO
        pass
