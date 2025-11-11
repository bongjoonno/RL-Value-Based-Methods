from src.rl_path_finder.model import Board
from src.rl_path_finder.constants import ALPHA, GAMMA, EPSILON

def sarsa_update(
    board: Board, 
    previous_state = None,
    previous_action = None, 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:

    current_state = (board.agent_position_y, board.agent_position_x)
    outcome = board.perform_move()
    current_action = board.chosen_action

    if outcome in ['finished course', 'Ran out of trials']: 
        return 'episode ended'

    elif previous_state is None:
        return current_state, current_action

    q = board.q_table[previous_state][previous_action]

    current_state_action_q_score = board.q_table[current_state][current_action]

    target = -1 + (gamma * current_state_action_q_score)

    board.q_table[previous_state][previous_action] += alpha * (target - q)

    return current_state, current_action

def sarsa_train(epochs):
    board = Board()

    previous_state, previous_action = None, None
    
    for _ in range(epochs)
        outcome = sarsa_update(board, previous_state, previous_action)
        
        if outcome == 'episode ended':
            board = Board()
        else:
            previous_state, previous_action = outcome
        
        Board.epsilon = max(0.01, Board.epsilon * 0.999)
        
    return Board.q_table