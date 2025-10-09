from board import Board
from constants import ALPHA, GAMMA

def q_learning(
    board: Board, 
    train_trial_limit: int , 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:

    for _ in range(train_trial_limit):
        cur_state = (board.agent_position_y, board.agent_position_x)
        
        outcome = board.perform_move()

        cur_action = board.chosen_action

        if outcome in ['finished course', 'Ran out of trials']: break
        
        board.get_next_move_prep()
        
        max_move_q_score = board.current_state_q_table[board.max_reward_move_for_state]

        target = -1 + (gamma * max_move_q_score)
        
        q = board.q_table[cur_state][cur_action]

        board.q_table[cur_state][cur_action] += alpha * (target - q)
    
        print(board.move_number)