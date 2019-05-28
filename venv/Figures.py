from abc import ABC, abstractmethod
import numpy as np

'''
In this module, we have all the figures


'''


def findKing(color):
    return list(filter(lambda it: it.getColor() == color and it.getName() == "King", Figure.chessboard.values()))[0]


def getAllFiguresOfOneColor(color):
    return list(filter(lambda it: it.getColor() != color, Figure.chessboard.values()))


def isChecked(x, y, enemyFigures):
    for figure in enemyFigures:
        if figure.movePossible(x, y):
            print(figure)
            return True
    return False


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

    '''
    this method is called by the player.move() method
    it first chekcs if the wanted move is possible, then makes it and checks if it is check afterwards.
    if that is the case, the move gets rejected   
    '''

    def move(self, x, y):
        if (x, y) in Figure.chessboard:
            if Figure.chessboard[(x, y)].getColor() == self._color:
                raise MoveError("Cant take own figure")
        if not self.movePossible(x, y):
            raise MoveError("")
        figureRemoved = False
        if (x, y) in Figure.chessboard:
            oldFigure = Figure.chessboard[(x,y)]
            figureRemoved = True
        Figure.chessboard.pop((self._x, self._y))
        oldx = self._x
        oldy = self._y
        self._x = x
        self._y = y
        Figure.chessboard[(x, y)] = self
        # check?
        king = findKing(self._color)
        enemyFigures = getAllFiguresOfOneColor(self._color)
        if isChecked(king.getCoordinates()[0], king.getCoordinates()[1], enemyFigures):
            if figureRemoved:
                Figure.chessboard[(x, y)] = oldFigure
            Figure.chessboard[(oldx, oldy)] = self
            raise MoveError("King in Danger")

    def getCoordinates(self):
        return (self._x, self._y)

    def getColor(self):
        return self._color

    def getName(self):
        return self._name

    def __repr__(self):
        return str((self._x, self._y)) + ", " + self._color


class King(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "King"

    # can do the following moves
    def movePossible(self, x, y):
        # king can't move more than one step in x or y direction
        if abs(self._x - x) <= 1 and abs(self._y - y) <= 1:  # both differences 1 -> diagonal step
            return True
        return False

    def __repr__(self):
        return "king, " + Figure.__repr__(self)


class Farmer(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Farmer"

    # evaluates if a move is possible and then calls the super function to do the move
    def movePossible(self, x, y):
        if self._color == "white":
            # move two steps from the starting position
            if self._x == x and self._y == 7 and y == 5 and not (x, 6) in Figure.chessboard and not (x,
                                                                                                     5) in Figure.chessboard:
                return True
            # move to last field and change figure
            if self._x == x and self._y == 1 and not (x, 1) in Figure.chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and self._y - y == 1 and not (x, y) in Figure.chessboard:
                return True
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == 1 and (x, y) in Figure.chessboard:
                if Figure.chessboard[(x, y)].getColor() != self._color:
                    return True
        if self._color == "black":
            # move two steps from the starting position
            if self._x == x and self._y == 2 and y == 4 and not (x, 4) in Figure.chessboard and not (x,
                                                                                                     3) in Figure.chessboard:
                return True
            # move to last field and change figure
            if self._x == x and self._y == 8 and not (x, 8) in Figure.chessboard:
                raise NotImplementedError
            # move one step forward
            if self._x == x and y - self._y == 1 and not (x, y) in Figure.chessboard:
                return True
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == -1 and (x, y) in Figure.chessboard:
                if Figure.chessboard[(x, y)].getColor() != self._color:
                    return True
        return False

    def __repr__(self):
        return "Farmer, " + Figure.__repr__(self)


class Rock(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Rock"

    # evaluates if a move is possible and then calls the super function to do the move
    def movePossible(self, x, y):
        if self._y == y:
            if not list(filter(lambda xIt: (xIt, y) in Figure.chessboard,
                               range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)))):
                return True
        if self._x == x:
            if not list(filter(lambda yIt: (x, yIt) in Figure.chessboard,
                               range(self._y + np.sign(y - self._y), y, np.sign(y - self._y)))):
                return True
        return False

    def __repr__(self):
        return "Rock, " + Figure.__repr__(self)


class Knight(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Knight"

    # evaluates if a move is possible and then calls the super function to do the move
    def movePossible(self, x, y):
        if (abs(self._x - x) == 2 and abs(self._y - y) == 1) or (abs(self._y - y) == 2 and abs(self._x - x) == 1):
            return True
        return False


def __repr__(self):
    return "Knight, " + Figure.__repr__(self)


class Bishop(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Bishop"

    # evaluates if a move is possible and then calls the super function to do the move
    def movePossible(self, x, y):
        if abs(self._x - x) == abs(self._y - y):
            if not list(filter(lambda it: it in Figure.chessboard,
                               zip(range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)),
                                   range(self._y + np.sign(y - self._y), y, np.sign(y - self._y))))):
                return True
        return False

    def __repr__(self):
        return "Bishop, " + Figure.__repr__(self)


class Queen(Bishop, Rock):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Queen"

    def move(self, x, y):

        if Bishop.movePossible(self, x, y):
            return True

        if Rock.move(self, x, y):
            return True

        return False


def __repr__(self):
    return "Queen, " + Figure.__repr__(self)


class MoveError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__("This move is not possible for " + message)
