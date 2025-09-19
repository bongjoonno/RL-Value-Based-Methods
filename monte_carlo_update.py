from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward

def monte_carlo_update(board: BoardMultiDimensional, alpha=0.1):
    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, discounted_rewards = [])

    for j in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][j]
        cur_action = board.trajectories['action'][j]
        target = discounted_rewards[j]

        q = board.state_action_average_reward[cur_state][cur_action]

        board.state_action_average_reward[cur_state][cur_action] += alpha * (target - q)