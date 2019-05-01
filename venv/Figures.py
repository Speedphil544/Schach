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
        # alte != neue Position
        chessboard[(x, y)] = self

    def getCoordinates(self):
        return (self._x, self._y)

    def getColor(self):
        return self._color

    def __repr__(self):
        return str((self._x, self._y)) + ", " + self._color


class King(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # can do the following moves
    def move(self, x, y, chessboard):
        # king can't move more than one step in x or y direction
        if abs(self._x - x) <= 1 and abs(self._y - y) <= 1:  # both differences 1 -> diagonal step
            super().move(x, y, chessboard)

    def __repr__(self):
        return "king, " + super().__repr__()


# class for the farmer figure
class Farmer(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y, chessboard):
        if self._color == "white":
            # move two steps from the starting position
            if self._x == x and self._y == 7 and y == 5 and not (x, 6) in chessboard and not (x, 5) in chessboard:
                super().move(x, y, chessboard)
                return
            # move to last field and change figure
            if self._x == x and self._y == 1 and not (x, 1) in chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and self._y - y == 1 and not (x, y) in chessboard:
                super().move(x, y, chessboard)
                return
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == 1 and (x, y) in chessboard:
                if chessboard[(x, y)].getColor() != self._color:
                    super().move(x, y, chessboard)
                    return
        if self._color == "black":
            # move two steps from the starting position
            if self._x == x and self._y == 2 and y == 4 and not (x, 4) in chessboard and not (x, 3) in chessboard:
                super().move(x, y, chessboard)
                return
            # move to last field and change figure
            if self._x == x and self._y == 8 and not (x, 8) in chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and y - self._y == 1 and not (x, y) in chessboard:
                super().move(x, y, chessboard)
                return
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == -1 and (x, y) in chessboard:
                if chessboard[(x, y)].getColor() != self._color:
                    super().move(x, y, chessboard)
                    return
            raise NotImplementedError

    def __repr__(self):
        return "farmer, " + super().__repr__()


chessboard = {}
chessboard[(2, 6)] = Farmer(2, 6, "black")
chessboard[(1, 7)] = Farmer(1, 7, "white")
chessboard[(1, 6)] = EmptyFigure()
chessboard[(1, 5)] = EmptyFigure()
chessboard[(1, 7)].move(3, 6, chessboard)
