from Figures import *


class Player:
    def __init__(self, color):
        assert color == "white" or color == "black"
        self._figures = []
        if color == "white":
            for x in range(1, 9):
                self._figures.append(Farmer(x, 6, color))

            self._figures.append(Rock(1, 8, color))
            self._figures.append(Rock(8, 8, color))
            self._figures.append(Knight(2, 8, color))
            self._figures.append(Knight(7, 8, color))
            self._figures.append(Bishop(3, 8, color))
            self._figures.append(Bishop(6, 8, color))
            self._figures.append(King(4, 8, color))
            self._figures.append(Bishop(5, 8, color))


Player("white")
print (Figure.chessboard)
