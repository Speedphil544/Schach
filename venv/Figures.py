from abc import ABC, abstractmethod
import numpy as np

'''
In this module, we have all the figures
'''


# checks if it is checkmate
def isCheckmate(color):
    king = findKing(color)
    enemyFigures = getAllFiguresOfOneColor(color)
    x, y = king.getCoordinates()
    if not isChecked(x, y, enemyFigures):
        return False
    for y in range(1, 9):
        for x in range(1, 9):
            if not (x, y) in Figure.chessboard or (
                    (x, y) in Figure.chessboard and Figure.chessboard[(x, y)].getColor() != color):
                if king.movePossible(x, y):
                    if not isChecked(x, y, enemyFigures):
                        return False

        return True


# returns opposite color
def oppositeColor(color):
    if color == "White":
        return "Black"
    else:
        return "White"


# returns the king for the given color
def findKing(color):
    return list(filter(lambda it: it.getColor() == color and it.getName() == "King", Figure.chessboard.values()))[0]


# returns a list of all figures of the opposite color
def getAllFiguresOfOneColor(color):
    return list(filter(lambda it: it.getColor() != color, Figure.chessboard.values()))


# returns wether the figure this these coordinates could be attacked by any figure
def isChecked(x, y, enemyFigures):
    for figure in enemyFigures:
        if figure.movePossible(x, y):
            return True
    return False


# represents a figure on the board
class Figure(ABC):
    chessboard = {}
    gameEnded = False

    @abstractmethod
    def __init__(self, x, y, color):
        assert x in [1, 2, 3, 4, 5, 6, 7, 8] and y in [1, 2, 3, 4, 5, 6, 7, 8] and (
                color == "White" or color == "Black") and not (x, y) in Figure.chessboard
        self._x = x
        self._y = y
        self._color = color
        self._moved = False
        Figure.chessboard[(x, y)] = self

    '''
    this method is called by the player.move() method
    it first checks if the wanted move is possible, then makes it and checks if it is check afterwards.
    if that is the case, the move gets rejected. Return False if the move was not possible, True otherwise  
    '''

    def move(self, x, y):
        if (x, y) in Figure.chessboard:
            if Figure.chessboard[(x, y)].getColor() == self._color:
                return False
        if not self.movePossible(x, y):
            return False
        figureRemoved = False
        if (x, y) in Figure.chessboard:
            oldFigure = Figure.chessboard[(x, y)]
            figureRemoved = True
        Figure.chessboard.pop((self._x, self._y))
        oldx = self._x
        oldy = self._y
        self._x = x
        self._y = y
        Figure.chessboard[(x, y)] = self
        # if the king could be attacked by enemy figures, revert the move
        king = findKing(self._color)
        enemyFigures = getAllFiguresOfOneColor(self._color)
        if isChecked(king.getCoordinates()[0], king.getCoordinates()[1], enemyFigures):
            if figureRemoved:
                Figure.chessboard[(x, y)] = oldFigure
            else:
                Figure.chessboard.pop((x, y))
            Figure.chessboard[(oldx, oldy)] = self
            return False

        else:
            # check if moved figure is a farmer and change it to another figure
            if self._name == "Peasant" and (y == 1 and self._color == "White"
                                           or y == 8 and self._color == "Black"):
                chessboard[(x, y)] = Figure(x, y, self._color)
            # indicate that the figure has been moved at least once
            self._moved == True
            # end the game if it is checkmate
            if isCheckmate(oppositeColor(self.getColor())):
                Figure.gameEnded = True

            return True

    def getCoordinates(self):
        return (self._x, self._y)

    def getColor(self):
        return self._color

    def getName(self):
        return self._name

    def __repr__(self):
        return str(self.getName()[0] + self._color[0])

    def getMoved(self):
        return self._moved


class King(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "King"

    # can do the following moves
    def movePossible(self, x, y):
        # king can't move more than one step in x or y direction
        if abs(self._x - x) <= 1 and abs(self._y - y) <= 1:  # both differences 1 -> diagonal step
            return True
        # rochade
        if self._moved == False:
            if self._color == "White":
                if (x, y) == (7, 8) and (8, 8) in Figure.chessboard:
                    if Figure.chessboard[(8, 8)].getName() == "Rock" and Figure.chessboard[
                        (8, 8)].getMoved() == False and not (6,
                    8) in Figure.chessboard and not (7, 8) in Figure.chessboard:
                        enemyFigures = getAllFiguresOfOneColor("White")
                        if not isChecked(6, 8, enemyFigures) and not isChecked(7, 8, enemyFigures):
                            Figure.chessboard[(8, 8)].move(6, 8)
                            return True
                if (x, y) == (3, 8) and (1, 8) in chessboard:
                    if Figure.chessboard[(1, 8)].getName() == "Rock" and Figure.chessboard[
                        (1, 8)].getMoved() == False and not (2,
                    8) in Figure.chessboard and not (3, 8) in Figure.chessboard and not (4, 8) in Figure.chessboard:
                        enemyFigures = getAllFiguresOfOneColor("White")
                        if not isChecked(3, 8, enemyFigures) and not isChecked(4, 8, enemyFigures) and not isChecked(2,
                                                                                                                     8,
                                                                                                                     enemyFigures):
                            Figure.chessboard[(8, 8)].move(6, 8);
                            return True

            if self._color == "Black":
                if (x, y) == (7, 1) and (8, 1) in chessboard:
                    if Figure.chessboard[(8, 1)].getName() == "Rock" and Figure.chessboard[
                        (8, 1)].getMoved() == False and not (6,
                    1) in Figure.chessboard and not (7, 1) in Figure.chessboard:
                        enemyFigures = getAllFiguresOfOneColor("Black")
                        if not isChecked(6, 1, enemyFigures) and not isChecked(7, 1, enemyFigures):
                            Figure.chessboard[(8, 1)].move(6, 1);
                            return True
                if (x, y) == (3, 1) and (1, 1) in Figure.chessboard:
                    if Figure.chessboard[(1, 1)].getName() == "Rock" and Figure.chessboard[
                        (1, 1)].getMoved() == False and not (2,
                    1) in Figure.chessboard and not (3, 1) in Figure.chessboard and not (4, 1) in Figure.chessboard:
                        enemyFigures = getAllFiguresOfOneColor("Black")
                        if not isChecked(3, 1, enemyFigures) and not isChecked(4, 1, enemyFigures) and not isChecked(2,
                                                                                                                     1,
                                                                                                                     enemyFigures):
                            Figure.chessboard[(8, 1)].move(6, 1);
                            return True

        return False


class Peasant(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Peasant"

    def movePossible(self, x, y):
        if self._color == "White":
            # move two steps from the starting position
            if self._x == x and self._y == 7 and y == 5 and not (x, 6) in Figure.chessboard and not (x,
            5) in Figure.chessboard:
                return True
            # move one step forward
            if self._x == x and self._y - y == 1 and not (x, y) in Figure.chessboard:
                return True
            # take enemy figure
            if abs(self._x - x) == 1 and self._y - y == 1 and (x, y) in Figure.chessboard:
                if Figure.chessboard[(x, y)].getColor() != self._color:
                    return True
        if self._color == "Black":
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


class Rock(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Rock"

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


class Knight(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Knight"

    def movePossible(self, x, y):
        if (abs(self._x - x) == 2 and abs(self._y - y) == 1) or (abs(self._y - y) == 2 and abs(self._x - x) == 1):
            return True
        return False


class Bishop(Figure):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Bishop"

    def movePossible(self, x, y):
        if abs(self._x - x) == abs(self._y - y):
            if not list(filter(lambda it: it in Figure.chessboard,
                               zip(range(self._x + np.sign(x - self._x), x, np.sign(x - self._x)),
                                   range(self._y + np.sign(y - self._y), y, np.sign(y - self._y))))):
                return True
        return False


class Queen(Bishop, Rock):
    def __init__(self, x, y, color):
        Figure.__init__(self, x, y, color)
        self._name = "Queen"

    def movePossible(self, x, y):

        if Bishop.movePossible(self, x, y):
            return True

        if Rock.movePossible(self, x, y):
            return True

        return False
