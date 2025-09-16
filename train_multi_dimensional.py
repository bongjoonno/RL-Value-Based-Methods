from imports import pd, sleep
from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward
from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y, GAMMA_DISCOUNTED_REWARD
from imports import pickle


trajectories_arr = []

alpha = 0.05

epochs = 1

for _ in range(epochs):
    board = BoardMultiDimensional()
    board.perform_move()

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

#with open('/workspaces/monte-carlo/state_action_average_reward_2.pkl', 'wb') as f:
   # pickle.dump(state_action_average_reward, f)