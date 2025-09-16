from imports import pickle
from board import Board
from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'rb') as f:
    state_action_average_reward = pickle.load(f)

trials = 1_000

trial_results = []

for i, dict in state_action_average_reward.items():
    print(i, dict)

for _ in range(trials):
    board = Board(state_action_average_reward, epsilon = 0, limit=(COURSE_LENGTH_Y-1) + (COURSE_LENGTH_X-1))
    trial_results.append(board.perform_move())

accuracy = sum(trial_results) / len(trial_results)
print(accuracy)