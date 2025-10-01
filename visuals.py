from imports import sys

def clear_board_in_place(board_y_length):
    for _ in range(board_y_length):
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

def welcome_message():
    print("HELLO AND WELCOME TO THE REINFORCEMENT LEARNING GRID GAME\n")
    
    print("THE AI'S GOAL IS TO CONTROL PLAYER 'P' TO REACH THE END AT '1'\n")
    
    print('[P 0 0 0 0 0]\n'
          '[0 0 0 0 0 0]\n'
          '[0 0 0 0 0 1]\n')
    
    print("(p.s. the AI can move WASD)\n")