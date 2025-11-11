from board import Board
from constants import ALPHA, GAMMA
from imports import tqdm

def q_learning_update(
    board: Board,
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:

    
    cur_state = (board.agent_position_y, board.agent_position_x)
    
    outcome = board.perform_move()

    cur_action = board.chosen_action

    if outcome in ['finished course', 'Ran out of trials']:
        return 'episode ended'
    
    board.get_next_move_prep()
    
    max_move_q_score = board.current_state_q_table[board.max_reward_move_for_state]

    target = -1 + (gamma * max_move_q_score)
    
    q = board.q_table[cur_state][cur_action]

    board.q_table[cur_state][cur_action] += alpha * (target - q)

def q_learning_train(course_length_y, course_length_x, epochs, q_table, train_trial_limit, epsilon):
    board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
    
    for _ in tqdm(range(epochs)):
        outcome = q_learning_update(board)
        
        if outcome == 'episode ended':
            board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table
        
    return q_table