from board import Board

limit = 5

board = Board(limit = limit)

for i in range(10):
    board.perform_random_move()