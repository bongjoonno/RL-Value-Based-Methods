from src.rl_path_finder.model import Board
from src.rl_path_finder.constants import EPOCHS, ALPHA, GAMMA
from src.rl_path_finder.imports import np

def expected_sarsa_update(
    board: Board, 
    previous_state = None,
    previous_action = None, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    current_state = (board.agent_position_y, board.agent_position_x)
    
    board.get_next_move_prep()
    board.policy()
    
    current_state_q_scores = board.current_state_q_scores
    current_state_move_probabilities = board.current_moves_probabilities

    outcome = board.perform_move()
    current_action = board.chosen_action

    if outcome in ['finished course', 'Ran out of trials']: 
        return 'episode ended'
    
    elif previous_state is None:
        return current_state, current_action

    q = board.q_table[previous_state][previous_action]

    expected_value_of_current_state = np.sum(current_state_q_scores * current_state_move_probabilities)

    target = -1 + (gamma * expected_value_of_current_state)

    board.q_table[previous_state][previous_action] += alpha * (target - q)

    return current_state, current_action

def expected_sarsa_train():
    previous_state, previous_action = None, None
    board = Board()
    
    for _ in range(EPOCHS):
        outcome = expected_sarsa_update(board, previous_state, previous_action)
        
        if outcome == 'episode ended':
            board = Board()
        else:
            previous_state, previous_action = outcome
        
        Board.epsilon = max(0.01, Board.epsilon * 0.999)