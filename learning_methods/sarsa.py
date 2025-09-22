from board import Board
from constants import TRAINING_TRIAL_LIMIT, ALPHA, GAMMA

def sarsa(
    board: Board, 
    trial_limit = TRAINING_TRIAL_LIMIT, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    for _ in range(trial_limit):
        previous_state = board.previous_state
        previous_action = board.chosen_action

        current_state = (board.agent_position_y, board.agent_position_x)
        outcome = board.perform_move()
        current_action = board.chosen_action

        if outcome == 'finished course': 
            break
        elif board.move_number == 1:
            continue

        q = board.q_table[previous_state][previous_action]
        current_state_action_q_score = board.q_table[current_state][current_action]

        target = -1 + (gamma * current_state_action_q_score)

        board.q_table[previous_state][previous_action] += alpha * (target - q)