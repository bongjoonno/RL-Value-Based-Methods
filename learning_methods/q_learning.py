from board import Board
from constants import ALPHA, GAMMA

def q_learning(
    board: Board,
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:

    cur_state = (board.agent_position_y, board.agent_position_x)
    
    outcome = board.perform_move()

    cur_action = board.chosen_action

    if outcome in ['finished course', 'Ran out of trials']:
        return 'episode ended'
    elif outcome == 'finished training':
        return 'training ended'
    
    board.get_next_move_prep()
    
    max_move_q_score = board.current_state_q_table[board.max_reward_move_for_state]

    target = -1 + (gamma * max_move_q_score)
    
    q = board.q_table[cur_state][cur_action]

    board.q_table[cur_state][cur_action] += alpha * (target - q)

    print(board.move_number)