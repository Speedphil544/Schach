from abc import ABC, abstractmethod
import numpy as np

'''
In this module, we have all the figures


'''


# represents a figure on the board
class Figure(ABC):
    chessboard = {}

    @abstractmethod
    def __init__(self, x, y, color):
        assert x in [1, 2, 3, 4, 5, 6, 7, 8] and y in [1, 2, 3, 4, 5, 6, 7, 8] and (
                color == "white" or color == "black") and not (x, y) in Figure.chessboard
        self._x = x
        self._y = y
        self._color = color
        Figure.chessboard[(x, y)] = self

    # this method is called by the overwritten method in the inheriting class
    def move(self, x, y):
        if (x, y) in Figure.chessboard:
            if Figure.chessboard[(x, y)].getColor() == self._color:
                raise MoveError("")
        Figure.chessboard.pop(self._x, self._y)
        self._x = x
        self._y = y
        # alte != neue Position
        Figure.chessboard[(x, y)] = self

    def wasMoved(self, newx, newy):
        return (self._x != newx) or (self._y != newy)

    def getCoordinates(self):
        return (self._x, self._y)

    def getColor(self):
        return self._color

    def __repr__(self):
        return str((self._x, self._y)) + ", " + self._color


class King(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # can do the following moves
    def move(self, x, y):
        # king can't move more than one step in x or y direction
        if abs(self._x - x) <= 1 and abs(self._y - y) <= 1:  # both differences 1 -> diagonal step
            Figure.move(self, x, y)

    def __repr__(self):
        return "king, " + Figure.__repr__(self)


class Farmer(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y):
        if self._color == "white":
            # move two steps from the starting position
            if self._x == x and self._y == 7 and y == 5 and not (x, 6) in Figure.Figure.chessboard and not (x,                                                                                           5) in Figure.Figure.chessboard:
                Figure.move(self, x, y)
                return
            # move to last field and change figure
            if self._x == x and self._y == 1 and not (x, 1) in Figure.chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and self._y - y == 1 and not (x, y) in Figure.chessboard:
                Figure.move(self, x, y)
                return
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == 1 and (x, y) in Figure.chessboard:
                if Figure.chessboard[(x, y)].getColor() != self._color:
                    Figure.move(self, x, y)
                    return
        if self._color == "black":
            # move two steps from the starting position
            if self._x == x and self._y == 2 and y == 4 and not (x, 4) in Figure.chessboard and not (x,
                                                                                                     3) in Figure.chessboard:
                Figure.move(self, x, y)
                return
            # move to last field and change figure
            if self._x == x and self._y == 8 and not (x, 8) in Figure.chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and y - self._y == 1 and not (x, y) in Figure.chessboard:
                Figure.move(self, x, y)
                return
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == -1 and (x, y) in Figure.chessboard:
                if Figure.chessboard[(x, y)].getColor() != self._color:
                    Figure.move(self, x, y)
                    return
            raise NotImplementedError

    def __repr__(self):
        return "Farmer, " + Figure.__repr__(self)


class Rock(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y):
        if self._y == y:
            if not list(filter(lambda xIt: (xIt, y) in Figure.chessboard,
                               range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)))):
                Figure.move(self, x, y)
                return
        if self._x == x:
            if not list(filter(lambda yIt: (x, yIt) in Figure.chessboard,
                               range(self._y + np.sign(y - self._y), y, np.sign(y - self._y)))):
                Figure.move(self, x, y)
                return
        raise MoveError("Rock")

    def __repr__(self):
        return "Rock, " + Figure.__repr__(self)


class Knight(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

# evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y):
        if (abs(self._x - x) == 2 and abs(self._y - y) == 1) or (abs(self._y - y) == 2 and abs(self._x - x) == 1):
            Figure.move(self, x, y)
        return
        raise MoveError("Knight")

    def __repr__(self):
        return "Knight, " + Figure.__repr__(self)


class Bishop(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    # evaluates if a move is possible and then calls the super function to do the move
    def move(self, x, y):
        if abs(self._x - x) == abs(self._y - y):
            if not list(filter(lambda it: it in Figure.chessboard,
                               zip(range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)),
                                   range(self._y + np.sign(y - self._y), y, np.sign(y - self._y))))):
                Figure.move(self, x, y)
                return
        raise MoveError("Bishop")

    def __repr__(self):
        return "Bishop, " + Figure.__repr__(self)


class Queen(Bishop, Rock):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)

    def move(self, x, y):
        try:
            Bishop.move(self, x, y)
            return
        except:
            MoveError
        try:
            Rock.move(self, x, y)
            return
        except:
            MoveError

        raise MoveError("Queen")

    def __repr__(self):
        return "Queen, " + Figure.__repr__(self)


class MoveError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__("This move is not possible for " + message)
