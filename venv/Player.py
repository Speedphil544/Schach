from Figures import *


class Player:
    def __init__(self, color):
        assert color == "White" or color == "Black"
        self._figures = {}
        self.color = color
        if color == "White":
            for x in range(1, 9):
                self._figures[(x, 7)] = Peasant(x, 7, color)
            self._figures[(1, 8)] = Rock(1, 8, color)
            self._figures[(8, 8)] = Rock(8, 8, color)
            self._figures[(2, 8)] = Knight(2, 8, color)
            self._figures[(7, 8)] = Knight(7, 8, color)
            self._figures[(3, 8)] = Bishop(3, 8, color)
            self._figures[(6, 8)] = Bishop(6, 8, color)
            self._figures[(5, 8)] = King(5, 8, color)
            self._figures[(4, 8)] = Queen(4, 8, color)
        else:
            for x in range(1, 9):
                self._figures[(x, 2)] = Peasant(x, 2, color)
            self._figures[(1, 1)] = Rock(1, 1, color)
            self._figures[(8, 1)] = Rock(8, 1, color)
            self._figures[(2, 1)] = Knight(2, 1, color)
            self._figures[(7, 1)] = Knight(7, 1, color)
            self._figures[(3, 1)] = Bishop(3, 1, color)
            self._figures[(6, 1)] = Bishop(6, 1, color)
            self._figures[(5, 1)] = King(5, 1, color)
            self._figures[(4, 1)] = Queen(4, 1, color)

    def move(self):
        while True:
            inp = input(self.color + "`s turn: ")
            oldx = int(inp[0])
            oldy = int(inp[1])
            newx = int(inp[2])
            newy = int(inp[3])
            if (oldx, oldy) in Figure.chessboard:
                fig = Figure.chessboard[(oldx, oldy)]
                if fig.getColor() == self.color:
                    if fig.move(newx, newy):
                        break
            print("Wrong coordinates for the figure you want to move")



if __name__ == "__main__":
    player1 = Player("White")
    player2 = Player("Black")
    players = [player1, player2]
    while not Figure.gameEnded:

        for player in players:
            player.move()
            for y in range(0, 9):
                for x in range(0, 9):
                    if y == x == 0:
                        print("", end=" ")
                    elif y == 0 and x != 0:
                        print("", x, end=" ")
                    elif x == 0 and y != 0:
                        print(y, end=" ")
                    elif x != 0 and y != 0:
                        if not (x, y) in Figure.chessboard:
                            print("XX", end=" ")
                        else:
                            print(Figure.chessboard[(x, y)], end=" ")
                print(" ")
