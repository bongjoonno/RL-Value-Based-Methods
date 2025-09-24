from board import Board
from constants import ALPHA, GAMMA
from imports import np

def expected_sarsa(
    board: Board, 
    train_trial_limit: int, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    previous_state, previous_action = None, None
    
    for _ in range(train_trial_limit):
        current_state = (board.agent_position_y, board.agent_position_x)
        board.get_next_move_prep()
        
        current_state_q_scores = board.current_state_q_scores
        current_state_move_probabilities = board.current_moves_probabilities

        outcome = board.perform_move()
        current_action = board.chosen_action

        if outcome == 'finished course': 
            break
        elif previous_state is None:
            previous_state, previous_action = current_state, current_action
            continue

        q = board.q_table[previous_state][previous_action]

        expected_value_of_current_state = np.sum(current_state_q_scores * current_state_move_probabilities)

        target = -1 + (gamma * expected_value_of_current_state)

        board.q_table[previous_state][previous_action] += alpha * (target - q)

        previous_state, previous_action = current_state, current_action