from Figures import *


class Player:
    def __init__(self, color):
        assert color == "white" or color == "black"
        self._figures = {}
        self.color = color
        if color == "white":
            for x in range(1, 9):
                self._figures[(x, 7)] = Farmer(x, 7, color)
            self._figures[(1, 8)] = Rock(1, 8, color)
            self._figures[(8, 8)] = Rock(8, 8, color)
            self._figures[(2, 8)] = Knight(2, 8, color)
            self._figures[(7, 8)] = Knight(7, 8, color)
            self._figures[(3, 8)] = Bishop(3, 8, color)
            self._figures[(6, 8)] = Bishop(6, 8, color)
            self._figures[(4, 8)] = King(4, 8, color)
            self._figures[(5, 8)] = Bishop(5, 8, color)
        else:
            for x in range(1, 9):
                self._figures[(x, 2)] = Farmer(x, 2, color)
            self._figures[(1, 1)] = Rock(1, 1, color)
            self._figures[(8, 1)] = Rock(8, 1, color)
            self._figures[(2, 1)] = Knight(2, 1, color)
            self._figures[(7, 1)] = Knight(7, 1, color)
            self._figures[(3, 1)] = Bishop(3, 1, color)
            self._figures[(6, 1)] = Bishop(6, 1, color)
            self._figures[(4, 1)] = King(4, 1, color)
            self._figures[(5, 1)] = Bishop(5, 1, color)

    def move(self):
        while True:
            inp = input("Your turn: ")
            oldx = int(inp[0])
            oldy = int(inp[1])
            newx = int(inp[2])
            newy = int(inp[3])
            Figure.chessboard[(oldx, oldy)].move(newx, newy)

        # Exception
    # print("something went wrong, repeat")


player1 = Player("white")
player2 = Player("black")
players = [player1, player2]
while True:

    for player in players:
        print(player.color)
        player.move()
