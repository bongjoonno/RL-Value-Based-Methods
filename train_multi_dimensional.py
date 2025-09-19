from imports import pd, sleep, plt
from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward
from generate_q_score_table import gen_q_score_table
from constants import TRAINING_TRIAL_LIMIT

from imports import pickle

#RL value based methods have two things consists of two things, Q function and update rule

trajectories_arr = []

epsilon = 1

alpha = 0.3

epochs = 20_000

q_scores_table = gen_q_score_table()

for _ in range(epochs):
    board = BoardMultiDimensional(state_action_average_reward=q_scores_table, epsilon=epsilon)

    for i in range(TRAINING_TRIAL_LIMIT):
        outcome = board.perform_move()
        if outcome == 'finished course':
            break

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, discounted_rewards = [])

    for j in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][j]
        cur_action = board.trajectories['action'][j]
        target = discounted_rewards[j]

        q = board.state_action_average_reward[cur_state][cur_action]

        board.state_action_average_reward[cur_state][cur_action] += alpha * (target - q)
    
    epsilon = max(0.01, epsilon * 0.999)
    q_scores_table = board.state_action_average_reward
    #print(epsilon)

for state, actions in board.state_action_average_reward.items():
    print(state, actions)

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'wb') as f:
    pickle.dump(board.state_action_average_reward, f)