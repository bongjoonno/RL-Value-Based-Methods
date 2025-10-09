from imports import np, time
from constants import TRAIN_FACTOR

class Board:
    def __init__(self, course_length_y, course_length_x, q_table, trial_limit = None, epsilon=1, randomized=True):
        self.course_length_y = course_length_y
        self.course_length_x = course_length_x
        
        self.q_table = q_table
        self.trial_limit = trial_limit
        
        if self.trial_limit == None:
            self.trial_limit = TRAIN_FACTOR * course_length_y * course_length_x
        
        
        self.epsilon = epsilon 
        
        
        self.grid = [[0 for i in range(course_length_x)] for j in range(self.course_length_y)]
        self.grid[-1][-1] = 1
        

        if randomized:
            try:
                self.agent_position_y = np.random.randint(0, self.course_length_y-1)
            except ValueError:
                self.agent_position_y = 0
            
            self.agent_position_x = np.random.randint(0, self.course_length_x-1)
        
        else: 
            self.agent_position_y, self.agent_position_x = 0, 0
        
        self.finish_position = (self.course_length_y-1, self.course_length_x-1)

        self.grid[self.agent_position_y][self.agent_position_x] = 'P'

        self.trajectories = {'state' : [], 'action' : [], 'reward' : []}

        self.y_step_mappings = {'W' : -1, 'S' : 1}
        self.x_step_mappings = {'D' : 1, 'A' : -1}

        self.chosen_action = None

        self.penalty = -1
        
        self.move_number = 0

        self.current_state_q_table = {}

        self.max_reward_move_for_state = None

        self.current_moves_probabilities = []

        self.current_state_q_scores = []

    def perform_move(self):  
        if self.move_number == self.trial_limit:
            return 'Ran out of trials'
        
        #self.display_grid()
        #time.sleep(1)
        self.grid[self.agent_position_y][self.agent_position_x] = 0

        self.chosen_action = self.get_next_move()

        self.log_trajectory()

        self.previous_state = (self.agent_position_y, self.agent_position_x)
        self.update_cur_position()
        
        self.move_number += 1
        
        if (self.agent_position_y, self.agent_position_x) == self.finish_position:
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

    def update_current_state_q_table(self):
        self.current_state_q_table = self.q_table[(self.agent_position_y, self.agent_position_x)]
        self.current_state_q_scores = np.array(list(self.current_state_q_table.values()))
    
    def update_max_reward_move(self):
        self.max_reward_move_for_state = max(self.current_state_q_table, key = self.current_state_q_table.get)

    def update_available_moves(self):
        self.available_moves = list(self.current_state_q_table.keys())

    def policy(self):
        self.current_moves_probabilities =  []

        random_move_prob = self.epsilon / len(self.available_moves)

        for move in self.available_moves:
            if move == self.max_reward_move_for_state:
                self.current_moves_probabilities.append(1 - self.epsilon + random_move_prob)
            else:
                self.current_moves_probabilities.append(random_move_prob)
        
        self.current_moves_probabilities = np.array(self.current_moves_probabilities)

    def get_next_move_prep(self):
        self.update_current_state_q_table()
        self.update_max_reward_move()
        self.update_available_moves()

    def get_next_move(self):
        self.get_next_move_prep()
        
        if self.epsilon == 0:
            return self.max_reward_move_for_state
        
        elif self.epsilon == 1:
            return np.random.choice(self.available_moves)
        
        elif len(self.available_moves) == 1:
            return self.available_moves[0]

        elif all(x == 0 for x in self.current_state_q_scores):
            return np.random.choice(self.available_moves)

        self.policy()

        return np.random.choice(self.available_moves, p = self.current_moves_probabilities)