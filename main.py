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

    print(board.trajectories)