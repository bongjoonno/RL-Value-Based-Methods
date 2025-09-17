from imports import pd, sleep, plt
from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward
from imports import pickle


trajectories_arr = []

epsilon = 1

alpha = 0.05

epochs = 1_000

undiscounted_rewards = []

for _ in range(epochs):
    board = BoardMultiDimensional(1)
    board.perform_move()
#RL value based methods have two things consists of two things, Q function and update rule
    undiscounted_rewards.append(board.reward)

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, discounted_rewards = [])
    board.trajectories['Gt_reward'] = discounted_rewards

    for i in range(len(board.trajectories)):
        cur_state = board.trajectories.loc[i, 'state']
        cur_action = board.trajectories.loc[i, 'action']
        cur_discounted_reward = board.trajectories.loc[i, 'Gt_reward']

        target = board.state_action_average_reward[cur_state][cur_action]
        board.state_action_average_reward[cur_state][cur_action] += alpha * (cur_discounted_reward - target)
    
    epsilon = max(0.01, epsilon * 0.999)

for i, dict in board.state_action_average_reward.items():
    print(i, dict)

with open('/workspaces/monte-carlo/state_action_average_reward_multi.pkl', 'wb') as f:
    pickle.dump(board.state_action_average_reward, f)

#plt.plot([i for i in range(100)], undiscounted_rewards[4900:5000])
#plt.savefig('plot.png')