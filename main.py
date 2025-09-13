from board import Board
from discounted_reward import get_discounted_reward

limit = 5

board = Board(limit = limit)

for i in range(10):
    board.perform_random_move()

trajectories = board.trajectories

rewards = list(trajectories['reward'])
print(rewards)

discounted_rewards = get_discounted_reward(rewards)
trajectories['Gt_reward'] = discounted_rewards

print(trajectories)