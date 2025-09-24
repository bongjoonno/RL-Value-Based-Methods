from board import Board
from utils.discounted_reward import get_discounted_reward
from constants import ALPHA, GAMMA

def monte_carlo(
    board: Board, 
    train_trial_limit:int , 
    alpha = ALPHA, 
    gamma = GAMMA
) -> None:
    
    for _ in range(train_trial_limit):
        cur_state = (board.agent_position_y, board.agent_position_x)
        outcome = board.perform_move()
        cur_action = board.chosen_action

        if outcome == 'finished course': break

    rewards = list(board.trajectories['reward'])
    discounted_rewards = get_discounted_reward(rewards, gamma, Gt_reward = 0, discounted_rewards = [])

    for i in range(len(board.trajectories['state'])):
        cur_state = board.trajectories['state'][i]
        cur_action = board.trajectories['action'][i]
        target = discounted_rewards[i]

        q = board.q_table[cur_state][cur_action]

        board.q_table[cur_state][cur_action] += alpha * (target - q)