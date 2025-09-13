from imports import pd
from board import Board
from discounted_reward import get_discounted_reward

#len is 11

trajectories = pd.DataFrame(columns=['state', 'action', 'reward'])

for i in range(10):
    board = Board()
    board.perform_random_move()
    trajectories = pd.concat([trajectories, board.trajectories])

print(trajectories)

rewards = list(trajectories['reward'])

discounted_rewards = get_discounted_reward(rewards)
trajectories['Gt_reward'] = discounted_rewards

state_action_average_reward = {i: {-1 : 0, 1 : 0} for i in range(11)}

alpha = 0.1

for i in range(len(trajectories)):
    cur_state = trajectories.loc[i, 'state']
    cur_action = trajectories.loc[i, 'action']
    cur_reward = trajectories.loc[i, 'reward']

    target = state_action_average_reward[cur_state][cur_action]
    state_action_average_reward[cur_state][cur_action] += alpha * (cur_reward - target)

for i, dict in state_action_average_reward.items():
    pass#print(dict)

#print(trajectories)