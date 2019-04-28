from abc import ABC, abstractmethod


# represents a figure on the board
class Figure(ABC):
    @abstractmethod
    def __init__(self, x, y, color):
        assert x in [1, 2, 3, 4, 5, 6, 7, 8] and y in [1, 2, 3, 4, 5, 6, 7, 8] and (
                    color == "white" or color == "black")
        self._x = x
        self._y = y
        self._color = color

    # this method is called by the overwritten method in the inheriting class
    def move(self, x, y, chessboard):
        chessboard[(self._x, self._y)] = EmptyFigure
        self._x = x
        self._y = y
        chessboard[(x, y)] = self

    def getCoordinates(self):
        return (self._x, self._y)

    def __repr__(self):
        return str((self._x, self._y)) + ", " + self._color

# I'm going to add a king class here


# class for the farmer figure
class Farmer(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
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
chessboard[(1, 7)] = Farmer(1, 9, "white")
chessboard[(1, 6)] = EmptyFigure()
chessboard[(1, 5)] = EmptyFigure()
chessboard[(1, 7)].move(1, 5, chessboard)
print(chessboard[(1, 5)])
