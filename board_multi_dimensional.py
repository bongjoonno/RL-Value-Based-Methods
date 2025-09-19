from imports import pd, np, sleep
from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y

class BoardMultiDimensional:
    def __init__(self, state_action_average_reward, epsilon=1):
        self.state_action_average_reward = state_action_average_reward
        self.epsilon = epsilon 
        
        self.grid = [[0 for i in range(COURSE_LENGTH_X)] for j in range(COURSE_LENGTH_Y)]
        
        self.start_pos = [0, 0]

        self.cur_pos_y = self.start_pos[0]
        self.cur_pos_x = self.start_pos[1]

        self.grid[self.cur_pos_y][self.cur_pos_x] = 'P'

        self.finish_pos = [COURSE_LENGTH_Y-1, COURSE_LENGTH_X-1]

        self.penalty = -1

        self.reward = 0

        self.trajectories = {'state' : [], 'action' : [], 'reward' : []}

        self.y_moves = {'W' : -1, 'S' : 1}
        self.x_moves = {'D' : 1, 'A' : -1}
    
        self.avg_rewards_for_state_action = {}

        self.move = ''

    def perform_move(self):
        self.grid[self.cur_pos_y][self.cur_pos_x] = 0

        self.move = self.policy()
        
        self.trajectories['state'].append((self.cur_pos_y, self.cur_pos_x))
        self.trajectories['action'].append(self.move)
        self.trajectories['reward'].append(self.penalty)

        self.cur_pos_y += self.y_moves.get(self.move, 0)
        self.cur_pos_x += self.x_moves.get(self.move, 0)

        self.grid[self.cur_pos_y][self.cur_pos_x] = 'P'

        self.reward += self.penalty

        if [self.cur_pos_y, self.cur_pos_x] == self.finish_pos:
            return 'finished course'
        
        else: return 'continue'
    
    def display_grid(self):
        for row in self.grid:
            print(row)
        print('\n')

    def policy(self):
        self.avg_rewards_for_state_action = self.state_action_average_reward[(self.cur_pos_y, self.cur_pos_x)]
        moves = list(self.avg_rewards_for_state_action.keys())
        moves_q_scores = list(self.avg_rewards_for_state_action.values())

        max_reward_move = max(self.avg_rewards_for_state_action, key=self.avg_rewards_for_state_action.get)

        if self.epsilon == 0:
            return max_reward_move
        
        elif self.epsilon == 1:
            return np.random.choice(moves)
        
        elif len(moves) == 1:
            return moves[0]

        elif all(x == 0 for x in moves_q_scores):
            return np.random.choice(moves)
        
        move_probs_dict = {}

        move_probs_dict[max_reward_move] = 1 - self.epsilon

        moves_besides_max = len(moves) - 1

        for move in moves:
            if move != max_reward_move:
                move_probs_dict[move] = self.epsilon / moves_besides_max

        move_probs = list(move_probs_dict.values())
        return np.random.choice(moves, p = move_probs)
    
    def policy_q_learning(self):
        max_move = self.policy()
        return self.avg_rewards_for_state_action[max_move]