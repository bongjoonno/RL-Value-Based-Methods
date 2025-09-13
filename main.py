from imports import pd
from board import Board
from discounted_reward import get_discounted_reward

#len is 11
trajectories_arr = []
state_action_average_reward = {i: {-1 : 0, 1 : 0} for i in range(11)}

for i in range(10):
    board = Board()
    board.perform_random_move()

    rewards = list(board.trajectories['reward'])

    discounted_rewards = get_discounted_reward(rewards)
    board.trajectories['Gt_reward'] = discounted_rewards

    alpha = 0.1

    for i in range(len(board.trajectories)):
        cur_state = board.trajectories.loc[i, 'state']
        cur_action = board.trajectories.loc[i, 'action']
        cur_reward = board.trajectories.loc[i, 'reward']

        target = state_action_average_reward[cur_state][cur_action]
        state_action_average_reward[cur_state][cur_action] += alpha * (cur_reward - target)

for i, dict in state_action_average_reward.items():
    pass