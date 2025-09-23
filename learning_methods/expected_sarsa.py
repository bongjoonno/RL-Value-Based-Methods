from board import Board
from constants import TRAINING_TRIAL_LIMIT, ALPHA, GAMMA

def expected_sarsa(
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
        
        board.get_next_move_prep()
        board.policy()

        print(board.current_state_q_scores, board.current_moves_probabilities)
        expected_value_of_current_state = board.current_state_q_scores * board.current_moves_probabilities

        target = -1 + (gamma * expected_value_of_current_state)

        board.q_table[previous_state][previous_action] += alpha * (target - q)