from imports import pd, sleep
from board_multi_dimensional import BoardMultiDimensional
from generate_q_score_table import gen_q_score_table
from monte_carlo_update import monte_carlo_update
from q_learning_update import q_learning_update
from sarsa_update import sarsa_update
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TRAINING_TRIAL_LIMIT, GAMMA_DISCOUNTED_REWARD

from imports import pickle

#RL value based methods have two things consists of two things, Q function and update rule

trajectories_arr = []

epsilon = 1

alpha = 0.3

epochs = 20_000

q_scores_table = gen_q_score_table(COURSE_LENGTH_Y, COURSE_LENGTH_X)

for _ in range(epochs):
    board = BoardMultiDimensional(state_action_average_reward=q_scores_table, epsilon=epsilon, randomized=True)

    monte_carlo_update(board= board, trial_limit= TRAINING_TRIAL_LIMIT, alpha= alpha)
    #q_learning_update(board= board, alpha= alpha)
    
    epsilon = max(0.01, epsilon * 0.999)
    q_scores_table = board.state_action_average_reward
    #print(epsilon)

for state, actions in board.state_action_average_reward.items():
    print(state, actions)

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'wb') as f:
    pickle.dump(board.state_action_average_reward, f)