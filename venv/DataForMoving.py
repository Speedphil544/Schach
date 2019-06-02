import chess.pgn
import numpy as np
import tensorflow as tf



def getIndex(char):
    char = str(char)
    index = 0
    value = 1
    if char == 'K':
        index = 0
    elif char == 'Q':
        index = 1
    elif char == 'R':
        index = 2
    elif char == 'B':
        index = 3
    elif char == 'N':
        index = 4
    elif char == 'P':
        index = 5
    elif char == 'k':
        index = 0
        value = -1
    elif char == 'q':
        index = 1
        value = -1
    elif char == 'r':
        index = 2
        value = -1
    elif char == 'b':
        index = 3
        value = -1
    elif char == "n":
        index = 4
        value = -1
    elif char == "p":
        index = 5
        value = -1
    return index, value

def convertChessBoard(board, boardMatrix):
    for y in range(8):
        for x in range(8):
            piece = board.piece_at(8 * y + x)
            if piece:
                boardMatrix[y, x, getIndex(piece)[0]] = getIndex(piece)[1]





def createData(piece, size):
    pgn = open("C:/Users/User/Downloads/KingBase2019-pgn/KingBase2019-A00-A39.pgn")
    games = []
    labels = []
    for _ in range(size):
        game = chess.pgn.read_game(pgn)
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            if board.turn:
                boardMatrix = np.zeros((8, 8, 6))
                convertChessBoard(board, boardMatrix)
                x = move.to_square % 8
                y = int((move.to_square - x) / 8)
                if boardMatrix[y, x, 5] == piece:
                    boardMatrix[y, x, 5] = 0
                    label = np.zeros(64)
                    label[move.to_square] = 1
                    games.append(boardMatrix)
                    labels.append(label)

    games = np.array(games)
    labels = np.array(labels)
    return games, labels


