from imports import pickle
from board_multi_dimensional import BoardMultiDimensional
from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'rb') as f:
    state_action_average_reward = pickle.load(f)

trials = 100

trial_results = []

for state, actions in state_action_average_reward.items():
    print(state, actions)

trial_limit = (COURSE_LENGTH_Y-1) + (COURSE_LENGTH_X-1)

results_mappings = {'finished course' : 1, 'continue' : 0}

for _ in range(trials):
    board = BoardMultiDimensional(state_action_average_reward=state_action_average_reward, epsilon = 0)
    
    for i in range(trial_limit):
        res = board.perform_move()
    
    trial_results.append(results_mappings[res])

print('\n')
print(board.display_grid())

accuracy = sum(trial_results) / len(trial_results)
print(accuracy)