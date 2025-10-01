from imports import sys

def clear_board_in_place(board_y_length):
    for _ in range(board_y_length):
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")