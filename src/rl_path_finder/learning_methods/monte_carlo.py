from src.rl_path_finder.model import Board
from src.rl_path_finder.model import get_discounted_reward
from src.rl_path_finder.constants import EPOCHS, ALPHA


def monte_carlo_update(
    board: Board
) -> None:
    
    for _ in range(board.trial_limit):
        cur_state = (board.agent_position_y, board.agent_position_x)
        outcome = board.perform_move()
        cur_action = board.chosen_action

        if outcome in ['finished course', 'Ran out of trials']:
            break

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards)

    for i in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][i]
        cur_action = board.trajectories['action'][i]
        target = discounted_rewards[i]

        q = board.q_table[cur_state][cur_action]

        board.q_table[cur_state][cur_action] += ALPHA * (target - q)
    
def monte_carlo_train():
    board = Board()
    
    epochs = EPOCHS

    while epochs > 0:
        monte_carlo_update(board)
        
        Board.epsilon = max(0.01, Board.epsilon * 0.999)
        epochs -= board.move_number
        
        board = Board()