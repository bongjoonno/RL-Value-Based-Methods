from board import Board
from constants import TRAINING_TRIAL_LIMIT, ALPHA, GAMMA

def sarsa(
    board: Board, 
    trial_limit = TRAINING_TRIAL_LIMIT, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    for _ in range(trial_limit):
        cur_state = (board.cur_pos_y, board.cur_pos_x)
        outcome = board.perform_move()
        cur_action = board.move

        if outcome == 'finished course': break
        elif not board.prev_move:
            continue

        q = board.state_action_average_reward[board.prev_position][board.prev_move]
        cur_avg_reward = board.state_action_average_reward[cur_state][cur_action]

        target = -1 + (gamma * cur_avg_reward)

        board.state_action_average_reward[board.prev_position][board.prev_move] += alpha * (target - q)