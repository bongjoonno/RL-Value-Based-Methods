from imports import pd, np, sleep
from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y

class Board:
    def __init__(self, q_table, epsilon=1, randomized=True):
        self.q_table = q_table
        self.epsilon = epsilon 
        
        self.grid = [[0 for i in range(COURSE_LENGTH_X)] for j in range(COURSE_LENGTH_Y)]

        if randomized:
            self.agent_position_y = np.random.randint(0, COURSE_LENGTH_Y-1)
            self.agent_position_x = np.random.randint(0, COURSE_LENGTH_X-1)
        else: self.agent_position_y, self.agent_position_x = 0, 0

        self.agent_starting_state = (self.agent_position_y, self.agent_position_x)
        self.previous_state = self.agent_starting_state
        
        self.finish_pos = (COURSE_LENGTH_Y-1, COURSE_LENGTH_X-1)

        self.grid[self.agent_position_y][self.agent_position_x] = 'P'

        self.penalty = -1

        self.reward = 0

        self.trajectories = {'state' : [], 'action' : [], 'reward' : []}

        self.y_step_mappings = {'W' : -1, 'S' : 1}
        self.x_step_mappings = {'D' : 1, 'A' : -1}

        self.chosen_action = None

        self.move_number = 0

        self.current_state_q_scores = {}

    def perform_move(self):
        if self.agent_starting_state == self.finish_pos:
            return 'finished course'
        
        self.grid[self.agent_position_y][self.agent_position_x] = 0

        self.chosen_action = self.policy()

        self.log_trajectory()

        self.previous_state = (self.agent_position_y, self.agent_position_x)
        self.update_cur_position()

        self.reward += self.penalty
        self.move_number += 1

        if (self.agent_position_y, self.agent_position_x) == self.finish_pos:
            return 'finished course'
        else: 
            return 'continue'
    
    def log_trajectory(self):
        self.trajectories['state'].append((self.agent_position_y, self.agent_position_x))
        self.trajectories['action'].append(self.chosen_action)
        self.trajectories['reward'].append(self.penalty)

    def update_cur_position(self):
        self.agent_position_y += self.y_step_mappings.get(self.chosen_action, 0)
        self.agent_position_x += self.x_step_mappings.get(self.chosen_action, 0)
        self.grid[self.agent_position_y][self.agent_position_x] = 'P'

    def display_grid(self):
        for row in self.grid:
            print(row)
        print('\n')

    def get_current_state_q_score(self):
        self.current_state_q_scores = self.q_table[(self.agent_position_y, self.agent_position_x)]
    
    def get_max_reward_move_for_state(self):
        return max(self.current_state_q_scores, key = self.current_state_q_scores.get)

    def policy(self):
        self.get_current_state_q_score()

        moves = list(self.current_state_q_scores.keys())
        moves_q_scores = list(self.current_state_q_scores.values())

        max_reward_move = self.get_max_reward_move_for_state()

        if self.epsilon == 0:
            return max_reward_move
        
        elif self.epsilon == 1:
            return np.random.choice(moves)
        
        elif len(moves) == 1:
            return moves[0]

        elif all(x == 0 for x in moves_q_scores):
            return np.random.choice(moves)
        
        move_probs = []

        random_move_prob = self.epsilon / len(moves)

        for move in moves:
            if move == max_reward_move:
                move_probs.append(1 - self.epsilon + random_move_prob)
            else:
                move_probs.append(random_move_prob)

        return np.random.choice(moves, p = move_probs)