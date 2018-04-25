# the main controller
import Player
import Pieces
import Graph


class Game:
    def __init__(self, player1, player2):
        # TODO
        self.player1 = Player()
        self.player2 = Player()
        self.player1next = False
        self.tabla = Graph()

    def click(self, x, y, place):
        # TODO
        return False

    def getPieces(self):
        # TODO
        return [Pieces]

    def getMarked(self):
        # TODO
        return [Pieces]

    def getWinner(self):
        # TODO
        return 0
