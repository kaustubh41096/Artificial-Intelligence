#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from gameboard import *
from minmaxtree import *
import copy


def outcome(oldGame, column):
    newboard = maxConnect4Game()

    try:
        newboard.nodeDepth = oldGame.nodeDepth + 1
    except AttributeError:
        newboard.nodeDepth = 1

    newboard.pieceCount = oldGame.pieceCount
    newboard.gameBoard = copy.deepcopy(oldGame.gameBoard)

    if not newboard.gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not newboard.gameBoard[i][column]:
                newboard.gameBoard[i][column] = oldGame.currentTurn
                newboard.pieceCount += 1
                break

    if oldGame.currentTurn == 1:
        newboard.currentTurn = 2
    elif oldGame.currentTurn == 2:
        newboard.currentTurn = 1

    newboard.checkPieceCount()
    newboard.countScore()

    return newboard


def nextpossiblemove(gameboard):
    possiblemoves = []
    for x, y in enumerate(gameboard[0]):
        if y == 0:
            possiblemoves.append(x)
    return possiblemoves


def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:  # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)
    class_searchTree = Minimax(currentGame, depth)
    move_object = class_searchTree.minmax()
    currentGame.playPiece(move_object)

    print('\nMove no. %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, move_object + 1))
    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    elif currentGame.currentTurn == 2:
        currentGame.currentTurn = 1

    print('Game state after move:')
    currentGame.printGameBoard()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, depth):
    # Fill me in
    # sys.exit('Interactive mode is currently not implemented')
    while not currentGame.pieceCount == 42:
        if currentGame.currentTurn == 1:
            user = input("Enter the column number [1-7] : ")
            if not 0 < int(user) < 8:
                print("Enter number ranging from 1 to 7 ")
                continue
            if not currentGame.playPiece(int(user) - 1):
                print("column full")
                continue
            try:
                #human intended file
                currentGame.gameFile = open("file1.txt", 'w')
            except:
                sys.exit('Error opening file')

            print('Move number :' + str(currentGame.pieceCount) + ' Player :' + str(currentGame.currentTurn) +
                  ' column :' + str(int(user) + 1))
            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1

            print('Game state after move:')
            currentGame.printGameBoard()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

            currentGame.printGameBoardToFile()

        elif not currentGame.pieceCount == 42:
            Tree = Minimax(currentGame, depth)
            move = Tree.minmax()
            currentGame.playPiece(move)
            try:
                #computer intended file
                currentGame.gameFile = open("file2.txt", 'w')
            except:
                sys.exit('Error opening output file')
            print('\nMove no. %d: Player %d, column %d\n' % (
                currentGame.pieceCount, currentGame.currentTurn, move + 1))
            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1

            print('Game state after move:')
            currentGame.printGameBoard()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

            currentGame.printGameBoardToFile()

    currentGame.gameFile.close()

    if currentGame.player1Score > currentGame.player2Score:
        print("Player 1 wins")
    elif currentGame.player2Score > currentGame.player1Score:
        print ("AI (player 2) wins")
    else:
        print ("It's a draw")
    print("\nGame Over")


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()  # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    # print('Game state after move:')

    if game_mode == 'interactive':
        if argv[3] == 'computer-next':  # override current turn according to commandline arguments
            currentGame.currentTurn = 2
        else:  # human-next
            currentGame.currentTurn = 1
        interactiveGame(currentGame, argv[4])  # Be sure to pass whatever else you need from the command line
    else:  # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, argv[4])  # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)
