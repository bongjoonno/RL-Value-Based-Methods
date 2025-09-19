from board_multi_dimensional import BoardMultiDimensional
from constants import GAMMA_DISCOUNTED_REWARD

def q_learning_update(board: BoardMultiDimensional, cur_state, cur_action, alpha=0.1):
    max_move_avg_reward = board.policy_q_learning()
    target = -1 + (GAMMA_DISCOUNTED_REWARD * max_move_avg_reward)
    
    q = board.state_action_average_reward[cur_state][cur_action]

    board.state_action_average_reward[cur_state][cur_action] += alpha * (target - q)