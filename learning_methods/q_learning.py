from board_multi_dimensional import BoardMultiDimensional
from constants import TRAINING_TRIAL_LIMIT, ALPHA, GAMMA

def q_learning(
    board: BoardMultiDimensional, 
    trial_limit = TRAINING_TRIAL_LIMIT, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:

    for _ in range(trial_limit):
        cur_state = (board.cur_pos_y, board.cur_pos_x)
        outcome = board.perform_move()
        cur_action = board.move

        if outcome == 'finished course': break

        max_move_avg_reward = board.policy_q_learning()
        target = -1 + (gamma * max_move_avg_reward)
        
        q = board.state_action_average_reward[cur_state][cur_action]

        board.state_action_average_reward[cur_state][cur_action] += alpha * (target - q)