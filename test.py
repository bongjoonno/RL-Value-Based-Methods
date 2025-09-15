from imports import pickle
from board import Board
from constants import COURSE_LENGTH

with open('/workspaces/monte-carlo/state_action_average_reward.pkl', 'rb') as f:
    state_action_average_reward = pickle.load(f)

for i, dict in state_action_average_reward.items():
    print(i, dict)


trials = 100

for _ in range(trials):
    board = Board(state_action_average_reward, epsilon = 0, limit=COURSE_LENGTH-1)
    print(board.perform_move())
