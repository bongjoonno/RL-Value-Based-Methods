from board import Board
from constants import ALPHA, GAMMA

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

    if outcome == 'finished course': 
        return 'episode ended'

    elif previous_state is None:
        return current_state, current_action

    q = board.q_table[previous_state][previous_action]

    current_state_action_q_score = board.q_table[current_state][current_action]

    target = -1 + (gamma * current_state_action_q_score)

    board.q_table[previous_state][previous_action] += alpha * (target - q)

    return current_state, current_action

def sarsa_train(course_length_y, course_length_x, epochs, q_table, train_trial_limit, epsilon):
    previous_state, previous_action = None, None
    board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
    
    while epochs > 0:
        outcome = sarsa_update(board, previous_state, previous_action)
        
        if outcome == 'episode ended':
            board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
        else:
            previous_state, previous_action = outcome
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table
        epochs -= 1
        
    return q_table