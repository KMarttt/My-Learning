import math
from tictactoe import  player
from tictactoe import  winner
from tictactoe import  terminal
from tictactoe import  result

X = "X"
O = "O"
# player 2 is 0
EMPTY = None

my_list = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

single_list = [X, EMPTY, EMPTY]

print(single_list.count(EMPTY))

my_list1 = my_list[1]

print(my_list1.count(EMPTY))

# board = [[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]



# print(player(board))

# board = [[O, O, X],
#             [O, X, X],
#             [O, EMPTY, EMPTY]]

# board = [[O, O, X],
#             [X, O, X],
#             [O, EMPTY, O]]

# board = [[O, O, X],
#             [X, O, X],
#             [O, X, O]]

board = [[O, O, X],
            [X, O, X],
            [O, X, EMPTY]]

# print(winner((board)))

# print(terminal(board))

# if EMPTY in board[2]:
#     print("yes")

current_board = result(board, (2,2))
print(current_board)
print(winner(current_board))
print(terminal(current_board))
