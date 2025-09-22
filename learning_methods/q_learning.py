from board import Board
from constants import TRAINING_TRIAL_LIMIT, ALPHA, GAMMA

def q_learning(
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

        board.get_current_state_q_score()
        
        max_move = board.get_max_reward_move_for_state()
        max_move_q_score = board.cur_state_q_scores[max_move]

        target = -1 + (gamma * max_move_q_score)
        
        q = board.q_scores[cur_state][cur_action]

        board.q_scores[cur_state][cur_action] += alpha * (target - q)