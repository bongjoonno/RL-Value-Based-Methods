from board_multi_dimensional import BoardMultiDimensional
from discounted_reward import get_discounted_reward

def monte_carlo_update(board: BoardMultiDimensional, trial_limit, alpha=0.1, gamma=0.9):
    for _ in range(trial_limit):
        cur_state = (board.cur_pos_y, board.cur_pos_x)
        outcome = board.perform_move()
        cur_action = board.move

        if outcome == 'finished course': break

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, gamma, Gt_reward = 0, discounted_rewards = [])

    for i in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][i]
        cur_action = board.trajectories['action'][i]
        target = discounted_rewards[i]

        q = board.state_action_average_reward[cur_state][cur_action]

        board.state_action_average_reward[cur_state][cur_action] += alpha * (target - q)