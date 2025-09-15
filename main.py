from imports import pd, sleep
from board import Board
from discounted_reward import get_discounted_reward
from constants import COURSE_LENGTH

trajectories_arr = []
state_action_average_reward = {0: {1: 0}} | {i: {-1: 0, 1: 0} for i in range(1, COURSE_LENGTH-1)}

alpha = 0.05

epsilon = 0.5
epochs = 20_000

decrease_rate = epsilon / epochs

#best settings so far, alpha 0.01, epsilon 0.5,  epochs = 25

for _ in range(epochs):
    board = Board(state_action_average_reward, epsilon)
    board.perform_move()

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, discounted_rewards = [])
    board.trajectories['Gt_reward'] = discounted_rewards

    for i in range(len(board.trajectories)):
        cur_state = board.trajectories.loc[i, 'state']
        cur_action = board.trajectories.loc[i, 'action']
        cur_discounted_reward = board.trajectories.loc[i, 'Gt_reward']

        target = state_action_average_reward[cur_state][cur_action]
        state_action_average_reward[cur_state][cur_action] += alpha * (cur_discounted_reward - target)
    
    epsilon = max(0.01, epsilon * 0.999)

for i, dict in state_action_average_reward.items():
    print(i, dict)