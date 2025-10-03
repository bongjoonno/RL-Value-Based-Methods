from board import Board
from imports import sys, time

from visuals import clear_board_in_place
def has_perfect_accuracy(course_length_y, course_length_x, q_scores, testing_trial_limit, display_episode_path: bool) -> bool:
    board = Board(course_length_y, course_length_x, q_table = q_scores, epsilon = 0, randomized=False)
    
    print('\n')
    
    for _ in range(testing_trial_limit):
        if display_episode_path:
            board.display_grid()
            
            time.sleep(1)
            
            clear_board_in_place(board.course_length_y)
            
        res = board.perform_move()
    
    board.display_grid()
        
    return True if res == "finished course" else False