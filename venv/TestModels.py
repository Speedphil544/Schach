import chess.pgn
import numpy as np
import Figures as fg
import tensorflow as tf
import random as rm


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


pgn = open("C:/Users/User/Downloads/KingBase2019-pgn/KingBase2019-A00-A39.pgn")

modelPickField = tf.keras.models.load_model("Models/ModelPickField")
modelPawn = tf.keras.models.load_model("Models/ModelMovePawn")

for _ in range(2000):
    game = chess.pgn.read_game(pgn)
    board = chess.Board()
    for move in game.mainline_moves():
        boardMatrix = np.zeros((8, 8, 6))
        convertChessBoard(board, boardMatrix)
        boardMatrix = np.array([boardMatrix])
        a = modelPickField.predict(boardMatrix)[0, move.from_square]
        board.push(move)
        boardMatrix = np.zeros((8, 8, 6))
        convertChessBoard(board, boardMatrix)
        boardMatrix = np.array([boardMatrix])
        x = move.to_square % 8
        y = int((move.to_square - x) / 8)
        if board.turn and boardMatrix[0, y, x, 5] == -1:
            # a = np.array(a)
            # a = np.argmax(a)
            boardMatrix[0, y, x, 5] = 0
            b = modelPawn.predict(boardMatrix)[0, move.to_square]
            # b = np.array(b)
            # b = np.argmax(b)
            print("Predict: ", a, b)
            print("Real: ", move.from_square, move.to_square)

    print("ended")
