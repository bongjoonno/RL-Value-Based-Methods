from imports import pd, np, sleep, choices
from constants import COURSE_LENGTH

class Board:
    def __init__(self, state_action_average_reward, epsilon, limit=COURSE_LENGTH):
        self.limit = limit
        self.state_action_average_reward = state_action_average_reward
        self.epsilon = epsilon 

        self.grid = [0 for _ in range(COURSE_LENGTH-1)] + [1]
        
        self.cur_pos = 0
        
        self.finish_pos = len(self.grid) - 1

        self.penalty = -1

        self.trajectories = pd.DataFrame(columns=['state', 'action', 'reward'])

        self.get_opposite_move = {1 : -1, -1 : 1}

        self.move_probabilities = {}
        
    def perform_move(self):
        if self.cur_pos == self.finish_pos:
            return 'Reached end!'
        elif self.limit == 0:
            return f"Ran out of trials"

        self.grid[self.cur_pos] = 0

        move = int(self.policy())

        self.trajectories.loc[len(self.trajectories)] = [self.cur_pos, move, self.penalty]

        self.cur_pos += move

        self.grid[self.cur_pos] = 'P'

        self.limit -= 1

        #self.display_grid()
        #sleep(1)
        self.perform_move()
    
    def display_grid(self):
        print(self.grid)
    
    def policy(self):
        avg_rewards_for_state_action = self.state_action_average_reward[self.cur_pos]
        max_reward_move = max(avg_rewards_for_state_action, key=avg_rewards_for_state_action.get)
        
        if self.cur_pos > 0:
            opposite_move = self.get_opposite_move[max_reward_move]
            self.move_probabilities[max_reward_move] = 1 - self.epsilon
            self.move_probabilities[opposite_move]= self.epsilon

            move = choices(list(self.move_probabilities.keys()), weights = list(self.move_probabilities.values()))
            #print(self.move_probabilities, move)
            return move.pop()
        else:
            return 1