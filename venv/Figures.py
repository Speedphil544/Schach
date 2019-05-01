from abc import ABC, abstractmethod
import numpy as np

'''
In this module, we have all the figures


'''


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
        chessboard.pop(self._x, self._y)
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


class Tower(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y, chessboard):
        if (x, y) in chessboard:
            if chessboard[(x, y)].getColor() == self._color:
                raise NotImplementedError
        if self._y == y:
            if not list(filter(lambda xIt: (xIt, y) in chessboard,
                               range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)))):
                super().mover(x, y, chessboard)
                return
        if self._x == x:
            if not list(filter(lambda yIt: (x, yIt) in chessboard,
                               range(self._y + np.sign(y - self._y), y, np.sign(y - self._y)))):
                Figure.move(self, x, y, chessboard)
                return
        raise NotImplementedError


class Knight(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y, chessboard):
        if (x, y) in chessboard:
            if chessboard[(x, y)].getColor() == self._color:
                raise NotImplementedError
        if (abs(self._x - x) == 2 and abs(self._y - y) == 1) or (abs(self._y - y) == 2 and abs(self._x - x) == 1):
            Figure.move(self, x, y, chessboard)
            return
        raise NotImplementedError


class Bishop(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y, chessboard):
        if (x, y) in chessboard:
            if chessboard[(x, y)].getColor() == self._color:
                raise NotImplementedError
        if abs(self._x - x) == abs(self._y - y):
            if not list(filter(lambda it: it in chessboard,
                               zip(range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)),
                                   range(self._y + np.sign(y - self._y), y, np.sign(y - self._y))))):
                Figure.move(self, x, y, chessboard)
                return
        raise NotImplementedError


class Queen(Bishop, Tower):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    def move(self, x, y, chessboard):
        try:
            Bishop.move(self, x, y, chessboard)
            return
        except:
            NotImplementedError
        try:
            Tower.move(self, x, y, chessboard)
            return
        except:
            NotImplementedError
        raise NotImplementedError


chessboard = {}
chessboard[(3, 6)] = Farmer(1, 6, "black")
chessboard[(2, 7)] = Queen(2, 7, "white")
chessboard[(2, 7)].move(7, 5, chessboard)
