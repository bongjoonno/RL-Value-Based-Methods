from board_multi_dimensional import BoardMultiDimensional

def test_multi_dim(q_scores, trial_limit):
    trial_results = []

    results_mappings = {'finished course' : 1, 'continue' : 0}

    board = BoardMultiDimensional(state_action_average_reward = q_scores, epsilon = 0, randomized=False)

    for i in range(trial_limit):
        res = board.perform_move()

    trial_results.append(results_mappings[res])

    accuracy = sum(trial_results) / len(trial_results)
    return accuracy