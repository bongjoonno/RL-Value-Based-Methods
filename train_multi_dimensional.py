from imports import pd, sleep, plt
from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward
from generate_q_score_table import gen_q_score_table
from monte_carlo_update import monte_carlo_update
from q_learning_update import q_learning_update
from constants import TRAINING_TRIAL_LIMIT

from imports import pickle

#RL value based methods have two things consists of two things, Q function and update rule

trajectories_arr = []

epsilon = 1

alpha = 0.3

epochs = 10_000

q_scores_table = gen_q_score_table()

for _ in range(epochs):
    board = BoardMultiDimensional(state_action_average_reward=q_scores_table, epsilon=epsilon)

    for i in range(TRAINING_TRIAL_LIMIT):
        cur_state = (board.cur_pos_y, board.cur_pos_x)
        outcome = board.perform_move()
        cur_action = board.move

        if outcome == 'finished course':
            break
        else:
            q_learning_update(board, cur_state, cur_action, alpha)
        
    #monte_carlo_update(board, alpha)
    
    epsilon = max(0.01, epsilon * 0.999)
    q_scores_table = board.state_action_average_reward
    #print(epsilon)

for state, actions in board.state_action_average_reward.items():
    print(state, actions)

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'wb') as f:
    pickle.dump(board.state_action_average_reward, f)