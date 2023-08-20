"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    p = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                p += 1
    if board == initial_state():
        return X
    if p % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                action.add((row, col))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    x, y = action
    if 0 <= x <= 2 and 0 <= y <= 2:
        new_board[x][y] = player(board)
    return new_board


def verify_winner(board, player):
    if player == "Tie":
        if all(map(lambda x: all(x), board)):
            return "Tie"
    else:
        for i in range(3):
            suborder_player = 0
            for j in range(3):
                if board[i][j] == player:
                    suborder_player += 1
            if suborder_player == 3:
                return player

        for i in range(3):
            suborder_player = 0
            for j in range(3):
                if board[j][i] == player:
                    suborder_player += 1
            if suborder_player == 3:
                return player

        suborder_player = 0
        for x, y in {(0, 0), (1, 1), (2, 2)}:
            if board[x][y] == player:
                suborder_player += 1
        if suborder_player == 3:
            return player

        suborder_player = 0
        for x, y in {(0, 2), (1, 1), (2, 0)}:
            if board[x][y] == player:
                suborder_player += 1
        if suborder_player == 3:
            return player

    return None



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if verify_winner(board, X):
        return X
    elif verify_winner(board, O):
        return O
    elif verify_winner(board, "Tie"):
        return "Tie"
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    return None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winer = winner(board)
    if winer == X:
        return 1
    elif winer == O:
        return -1
    elif winer == "Tie":
        return 0
    
def min_value(state):
    if terminal(state):
        return utility(state), None
    v = float("inf")
    best_move = None
    actions_list = actions(state)
    for action in actions_list:
        new_board = result(state, action)
        new_v, _ = max_value(new_board)
        if new_v < v:
            v = new_v
            best_move = action
    return v, best_move

def max_value(state):
    if terminal(state):
        return utility(state), None
    v = float("-inf")
    best_move = None
    actions_list = actions(state)
    for action in actions_list:
        new_board = result(state, action)
        new_v, _ = min_value(new_board)
        if new_v > v:
            v = new_v
            best_move = action
    return v, best_move


def minimax(board):
    if terminal(board):
        return None
    cur_player = player(board)
    if cur_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    


if __name__ == "__main__":
    board = [
        [O, EMPTY, O],
        [EMPTY, X, EMPTY],
        [X, O, X]
    ]
    print(minimax(board))
