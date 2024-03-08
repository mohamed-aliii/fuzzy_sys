"""
Tic Tac Toe Player
"""
import copy
import math

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
    num_X = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)

    if num_X > num_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = []
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if board[i][j] is None:
                act.append((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None or action == (None, None):
        return board  # No action to perform, return unchanged board

    i, j = action
    if board[i][j] is not None:
        raise ValueError("Invalid action: cell already taken")
    else:
        new_board = copy.deepcopy(board)
        if player(board) == X:
            new_board[i][j] = "X"
        elif player(board) == O:
            new_board[i][j] = "O"

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

        # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

        # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    return all(cell is not None for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if not winner(board):
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0

def minimax_value(board):
    if terminal(board):
        return utility(board), None

    if player(board)==X:
        value = float('-inf')
        best_move = None
        for action in actions(board):
            score, _ = minimax_value(result(board, action))
            if score is not None and score > value:
                value = score
                best_move = action
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for action in actions(board):
            score, _ = minimax_value(result(board, action))
            if score is not None and score < value:
                value = score
                best_move = action
        return value, best_move


def minimax(board):
    """
    Returns the optimal move for the player to move on the board.
    """
    if terminal(board):
        return None

    best_move = None
    best_score = float('-inf') if player(board)==X else float('inf')

    for action in actions(board):
        score ,_= minimax_value(result(board, action))
        if score is not None:

            if (player(board)==X and score > best_score) or (not player(board)==X and score < best_score):
                best_score = score
                best_move = action

    return best_move