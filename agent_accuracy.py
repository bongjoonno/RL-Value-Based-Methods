from board import Board
from imports import sys, time
def has_perfect_accuracy(course_length_y, course_length_x, q_scores, testing_trial_limit, display_episode_path: bool) -> bool:
    board = Board(course_length_y, course_length_x, q_table = q_scores, epsilon = 0, randomized=False)
    
    for _ in range(testing_trial_limit):
        res = board.perform_move()
        
        if display_episode_path:
            board.display_grid()
            time.sleep(1)
            
            for _ in range(board.course_length_y):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
        
    return True if res == "finished course" else False