"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
# player 2 is 0
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    X_num = 0
    O_num = 0

    # If board is empty or there is an equal amount of X and O on the board: X turn
    #     this is because the O turn always comes 2nd, equalizing the number of X and Y on board
    # If the number of X is greater than O: O turn
    #     X turn is always first = more Y on board = hence, O turn next
    for sub_list in board:
        X_num += sub_list.count(X)
        O_num += sub_list.count(O)

    if X_num == 0 or X_num == O_num:
        return X
    elif X_num > O_num:
        return O

    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    set_action = set()
    row = 3
    column = 3
    # Row-major order
    for i in range(row):
        for j in range(column):
            if board[i][j] == EMPTY:
                move = (i,j)
                set_action.add(move)
    return set_action

    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError

def result(board, action):

    move = player(board)

    board_deepcopy = copy.deepcopy(board)
    board_deepcopy[action[0]][action[1]] = move
    return board_deepcopy


    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner_checker(list):
    if list.count(X) == 3:
        return X
    elif list.count(O) == 3:
        return O
    else:
        return None


def winner(board):
    # Initialization for readability
    row = 3
    column = 3

    # Row Major
    for horizontal_element in board:
        result_row = winner_checker(horizontal_element)
        if result_row: # If not None
            return result_row

    # Column Major
    for i in range(row):
        vertical_element = []
        for j in range(column):
            vertical_element.append(board[j][i])

        result_column = winner_checker(vertical_element)
        if result_column: # if not None
            return result_column

    # For Diagonal Left
    diagonal_element_left = [board[0][0], board[1][1], board[2][2]]

    diagonal_left_result = winner_checker(diagonal_element_left)
    if diagonal_left_result:
        return diagonal_left_result

    # For Diagonal Right
    diagonal_element_right = [board[0][2], board[1][1], board[2][0]]

    diagonal_right_result = winner_checker(diagonal_element_right)
    if diagonal_right_result:
        return diagonal_right_result

    # Return None if all checking returns None
    return None

    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError


def full_board(board):
    for sublist in board:
        if EMPTY in sublist:
            return False
    return True

def terminal(board):

    winner_result = winner(board)

    if winner_result == X or winner_result == O:
        return True
    elif full_board(board):
        return True
    else:
        return False


    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    # You may assume utility will only be called on a board if terminal(board) is True.
    winner_result = winner(board)

    if winner_result == X:
        return 1
    elif winner_result == O:
        return -1
    else:
        return 0



    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError






# assuming only O player will be AI
def minimax(board):
    """
        Returns the optimal action for the current player (X or O) based on the minimax algorithm.
        """
    if player(board) == X:
        _, action = max_value(board)
        return action
    elif player(board) == O:
        _, action = min_value(board)
        return action

    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 10
    best_action = None
    for action in actions(board):
        max_value_var, _ = max_value(result(board,action))
        # v = min(v, max_value_var)

        if max_value_var < v:
            v = max_value_var
            best_action = action

    return v, best_action

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -10
    best_action = None
    for action in actions(board):
        min_value_var, _ = min_value(result(board,action))
        if min_value_var > v:
            v = min_value_var
            best_action = action

    return v, best_action

