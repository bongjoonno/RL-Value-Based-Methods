from src.rl_path_finder.model import Board
from src.rl_path_finder.imports import time

from src.rl_path_finder.ui_io import clear_board_in_place

def has_perfect_accuracy(testing_trial_limit, display_episode_path: bool) -> bool:
    Board.trial_limit = testing_trial_limit
    board = Board(epsilon = 0, randomized = False)
    
    print('\n')
    
    for _ in range(testing_trial_limit):
        outcome = board.perform_move()
    
    if outcome == 'finished course':
        print(f'Found perfect path in {(Board.course_length_y-1) + (Board.course_length_x-1)} steps!')
    else:
        print('Perfect path not found... Displaying improperly learned path:')
        
    board = Board(epsilon = 0, randomized = False)
    
    print('\n')
    
    for _ in range(testing_trial_limit):
        if display_episode_path:
            board.display_grid()
            
            time.sleep(1)
            
            clear_board_in_place(board.course_length_y)
            
        outcome = board.perform_move()
    
    board.display_grid()
        
    return True if outcome == "finished course" else False