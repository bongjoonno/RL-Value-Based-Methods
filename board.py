from imports import pd, np, sleep
from constants import COURSE_LENGTH, TRAINING_TRIAL_LIMIT

class Board:
    def __init__(self, state_action_average_reward, epsilon, limit=TRAINING_TRIAL_LIMIT):
        self.limit = limit
        self.state_action_average_reward = state_action_average_reward
        self.epsilon = epsilon 

        self.grid = [0 for _ in range(COURSE_LENGTH-1)] + [1]
        
        self.cur_pos = 0
        
        self.finish_pos = COURSE_LENGTH-1

        self.penalty = -1

        self.trajectories = pd.DataFrame(columns=['state', 'action', 'reward'])

        self.get_opposite_move = {1 : -1, -1 : 1}
        
    def perform_move(self):
        if self.cur_pos == self.finish_pos:
            return 1
        elif self.limit == 0:
            return 0

        self.grid[self.cur_pos] = 0

        move = int(self.policy())
        
        self.trajectories.loc[len(self.trajectories)] = [self.cur_pos, move, self.penalty]

        self.cur_pos += move

        self.grid[self.cur_pos] = 'P'

        self.limit -= 1

        #self.display_grid()
        #sleep(1)
        return self.perform_move()
    
    def display_grid(self):
        print(self.grid)
    
    def policy(self):
        avg_rewards_for_state_action = self.state_action_average_reward[self.cur_pos]
        max_reward_move = max(avg_rewards_for_state_action, key=avg_rewards_for_state_action.get)
        
        if self.cur_pos > 0:
            opposite_move = self.get_opposite_move[max_reward_move]
            move_probs = {max_reward_move: 1 - self.epsilon, opposite_move : self.epsilon}
            move = np.random.choice(list(move_probs.keys()), p = list(move_probs.values()))
            #print(self.move_probs)
            return move
        else:
            return 1