from board import Board
from imports import sleep

def test(q_scores, trial_limit):
    trial_results = []

    results_mappings = {'finished course' : 1, 'continue' : 0}

    board = Board(q_table = q_scores, epsilon = 0, randomized=False)

    for i in range(trial_limit):
        res = board.perform_move()
        board.display_grid()
        sleep(1)

    trial_results.append(results_mappings[res])

    accuracy = sum(trial_results) / len(trial_results)
    return accuracy