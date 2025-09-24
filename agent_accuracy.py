from board import Board
from imports import sleep

def has_perfect_accuracy(course_length_y, course_length_x, q_scores, trial_limit, display_episode_path: bool) -> bool:
    board = Board(course_length_y, course_length_x, q_table = q_scores, epsilon = 0, randomized=False)
    
    for _ in range(trial_limit):
        res = board.perform_move()
        
        if display_episode_path:
            board.display_grid()
            sleep(1)
        
    return True if res == "finished course" else False