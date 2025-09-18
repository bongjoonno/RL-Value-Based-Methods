from imports import pd, sleep, plt
from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward
from generate_q_score_table import gen_q_score_table

from imports import pickle

#RL value based methods have two things consists of two things, Q function and update rule

trajectories_arr = []

epsilon = 1

alpha = 0.3

epochs = 30_000

q_scores_table = gen_q_score_table()

for _ in range(epochs):
    board = BoardMultiDimensional(state_action_average_reward=q_scores_table, epsilon=epsilon)
    board.perform_move()

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, discounted_rewards = [])

    for i in range(len(board.trajectories)):
        cur_state = board.trajectories['state'][i]
        cur_action = board.trajectories['action'][i]
        target = discounted_rewards[i]

        Q = board.state_action_average_reward[cur_state][cur_action]

        board.state_action_average_reward[cur_state][cur_action] += alpha * (target - Q)
    
    epsilon = max(0.01, epsilon * 0.999)
    q_scores_table = board.state_action_average_reward
    #print(epsilon)

for state, actions in board.state_action_average_reward.items():
    print(state, actions)

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'wb') as f:
    pickle.dump(board.state_action_average_reward, f)