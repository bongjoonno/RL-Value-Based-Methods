from board import Board
from utils.discounted_reward import get_discounted_reward
from constants import ALPHA, GAMMA


def monte_carlo_update(
    board: Board,
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    for _ in range(board.trial_limit):
        cur_state = (board.agent_position_y, board.agent_position_x)
        outcome = board.perform_move()
        cur_action = board.chosen_action

        if outcome in ['finished course', 'Ran out of trials']:
            break

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, GAMMA, Gt_reward = 0, discounted_rewards = [])

    for i in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][i]
        cur_action = board.trajectories['action'][i]
        target = discounted_rewards[i]

        q = board.q_table[cur_state][cur_action]

        board.q_table[cur_state][cur_action] += alpha * (target - q)
    
def monte_carlo(course_length_y, course_length_x, epochs, q_table, train_trial_limit, epsilon):
    board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
    
    while epochs > 0:
        monte_carlo_update(board)
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table
        epochs -= board.move_number
        
        board = Board(course_length_y, course_length_x, q_table, trial_limit = train_trial_limit, epsilon = epsilon)
        print(epochs)
    return q_table