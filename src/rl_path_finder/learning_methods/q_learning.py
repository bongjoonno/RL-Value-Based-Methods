from src.rl_path_finder.model import Board
from src.rl_path_finder.constants import EPOCHS, ALPHA, GAMMA
from src.rl_path_finder.imports import tqdm

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

def q_learning_train():
    board = Board()
    
    for _ in range(EPOCHS):
        outcome = q_learning_update(board)
        
        if outcome == 'episode ended':
            board = Board()
        
        Board.epsilon = max(0.01, Board.epsilon * 0.999)