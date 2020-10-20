from start import *


class Minimax:
    def __init__(self, game, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxDepth = int(depth)

    def minmax(self):
        minvalues = []
        possibleMoves = nextpossiblemove(self.game.gameBoard)
        for move in possibleMoves:
            result = outcome(self.game, move)
            minvalues.append(self.minval(result, 99999, -99999))
        choosen = possibleMoves[minvalues.index(max(minvalues))]
        return choosen

    def minval(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
            if self.currentTurn == 1:
                utility = state.player1Score * 2 - state.player2Score
            elif self.currentTurn == 2:
                utility = state.player2Score * 2 - state.player1Score
            return utility
        value = 99999
        for m in nextpossiblemove(state.gameBoard):
            newstate = outcome(state, m)
            value = min(value, self.maxval(newstate, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def maxval(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
            if self.currentTurn == 1:
                utility = state.player1Score * 2 - state.player2Score
            elif self.currentTurn == 2:
                utility = state.player2Score * 2 - state.player1Score
            return utility
        value = -99999
        for m in nextpossiblemove(state.gameBoard):
            newstate = outcome(state, m)
            value = max(value, self.minval(newstate, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value


