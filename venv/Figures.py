from abc import ABC, abstractmethod


# represents a figure on the board
class Figure(ABC):
    @abstractmethod
    def __init__(self, x, y, color):
        assert x, y in [1, 2, 3, 4, 5, 6, 7, 8] and (color == "white" or color == "black")
        self._x = x
        self._y = y
        self._color = color

    # when the figure is moved by one of the players
    def move(self, x, y, chessboard):
        chessboard[(self._x, self._y)] = EmptyFigure
        self._x = x
        self._y = y
        # alte != neue Position
        chessboard[(x, y)] = self

    def getCoordinates(self):
        return (self._x, self._y)

    def __repr__(self):
        return str((self._x, self._y)) + ", " + self._color

class King(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # can do the following moves
    def move(self, x, y, chessboard):
        # king can't move more than one step in x or y direction
        if abs(self._x - x) <= 1 and abs(self._y - y) <= 1: # both differences 1 -> diagonal step
            super().move(x, y, chessboard)

    def __repr__(self):
        return "king, " + super().__repr__()


class Farmer(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # can do the following moves
    def move(self, x, y, chessboard):
        if self._color == "white":
            if self._x == x and self._y == 7 and y == 5 and isinstance(
                    chessboard[(x, 6)], EmptyFigure) and isinstance(
                chessboard[(x, 5)], EmptyFigure):
                super().move(x, y, chessboard)

    def __repr__(self):
        return "farmer, " + super().__repr__()


class EmptyFigure:
    def __repr__(self):
        return "empty Field"


chessboard = {}
chessboard[(1, 7)] = Farmer(1, 7, "white")
chessboard[(1, 6)] = EmptyFigure()
chessboard[(1, 5)] = EmptyFigure()
chessboard[(1, 7)].move(1, 5, chessboard)
print(chessboard[(1, 5)])
