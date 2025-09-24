from board import Board
from imports import sleep

def has_perfect_accuracy(q_scores, trial_limit, display_episode_path: bool) -> bool:
    trial_results = []

    results_mappings = {'finished course' : 1, 'continue' : 0}

    board = Board(q_table = q_scores, epsilon = 0, randomized=False)
    
    if display_episode_path:
        for _ in range(trial_limit):
            res = board.perform_move()
            board.display_grid()
            sleep(1)

    trial_results.append(results_mappings[res])
    print(any(trial_results))
    return any(trial_results)