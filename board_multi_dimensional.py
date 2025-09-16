from imports import pd, np, sleep
from constants import COURSE_LENGTH, TRAINING_TRIAL_LIMIT, COURSE_LENGTH_X, COURSE_LENGTH_Y

class BoardMultiDimensional:
    def __init__(self, state_action_average_reward, epsilon=0.5, limit=TRAINING_TRIAL_LIMIT):
        self.limit = limit
        self.state_action_average_reward = state_action_average_reward
        self.epsilon = epsilon 

        self.grid = [[0 for i in range(COURSE_LENGTH_X)] for j in range(COURSE_LENGTH_Y)]
        
        self.start_pos = [0, 0]

        self.cur_pos_y = self.start_pos[0]
        self.cur_pos_x = self.start_pos[1]

        self.grid[self.cur_pos_y][self.cur_pos_x] = 'P'
        
        self.valid_moves = []

        self.finish_pos = COURSE_LENGTH-1

        self.penalty = -1

        self.trajectories = pd.DataFrame(columns=['state', 'action', 'reward'])

        self.get_opposite_move = {1 : -1, -1 : 1}
    
    def get_valid_moves(self):
        self.valid_moves = []

        if self.cur_pos_y > 0: 
            self.valid_moves.append('W')
        if self.cur_pos_x > 0:
            self.valid_moves.append('A')
        if self.cur_pos_y < 2:
            self.valid_moves.append('S')
        if self.cur_pos_x < 2:
            self.valid_moves.append('D')

    def perform_move(self):
        if self.cur_pos == self.finish_pos:
            return 1
        elif self.limit == 0:
            return 0

        self.grid[self.cur_pos] = 0

        move = int(self.policy())
        
        self.trajectories.loc[len(self.trajectories)] = [(self.cur_pos_y, self.cur_pos_x), move, self.penalty]

        self.cur_pos += move

        self.grid[self.cur_pos] = 'P'

        self.limit -= 1

        #self.display_grid()
        #sleep(1)
        return self.perform_move()
    
    def display_grid(self):
        print(self.grid)
    
    def policy(self):
        avg_rewards_for_state_action = self.state_action_average_reward[(self.cur_pos_y, self.cur_pos_x)]
        max_reward_move = max(avg_rewards_for_state_action, key=avg_rewards_for_state_action.get)
        
        if self.cur_pos > 0:
            opposite_move = self.get_opposite_move[max_reward_move]
            move_probs = {max_reward_move: 1 - self.epsilon, opposite_move : self.epsilon}
            move = np.random.choice(list(move_probs.keys()), p = list(move_probs.values()))
            #print(self.move_probs)
            return move
        else:
            return 1