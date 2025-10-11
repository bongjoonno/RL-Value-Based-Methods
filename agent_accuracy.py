from board import Board
from imports import sys, time

from visuals import clear_board_in_place
def has_perfect_accuracy(course_length_y, course_length_x, q_scores, testing_trial_limit, display_episode_path: bool) -> bool:
    board = Board(course_length_y, course_length_x, q_scores, testing_trial_limit, epsilon = 0, randomized = False)
    
    print('\n')
    
    for _ in range(testing_trial_limit):
        outcome = board.perform_move()
    
    if outcome == 'finished course':
        print(f'Found perfect path in {(course_length_y-1) + (course_length_x-1)} steps!')
    else:
        print('Perfect path not found... Displaying improperly learned path:')
        
    board = Board(course_length_y, course_length_x, q_scores, testing_trial_limit, epsilon = 0, randomized = False)
    
    print('\n')
    
    for _ in range(testing_trial_limit):
        if display_episode_path:
            board.display_grid()
            
            time.sleep(1)
            
            clear_board_in_place(board.course_length_y)
            
        outcome = board.perform_move()
    
    board.display_grid()
        
    return True if outcome == "finished course" else False