from imports import pd, np, sleep
from constants import TRAINING_TRIAL_LIMIT, COURSE_LENGTH_X, COURSE_LENGTH_Y

class BoardMultiDimensional:
    def __init__(self, epsilon=1, limit=TRAINING_TRIAL_LIMIT):
        self.epsilon = epsilon 
        self.limit = limit

        self.grid = [[0 for i in range(COURSE_LENGTH_X)] for j in range(COURSE_LENGTH_Y)]

        self.state_action_average_reward = {(i, j): {} for i in range(COURSE_LENGTH_Y) for j in range(COURSE_LENGTH_X)}

        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                if j < len(row) - 1:
                    self.state_action_average_reward[(i, j)]['D'] = 0
                if j > 0:
                    self.state_action_average_reward[(i, j)]['A'] = 0
                if i < len(self.grid) - 1:
                    self.state_action_average_reward[(i, j)]['S'] = 0
                if i > 0:
                    self.state_action_average_reward[(i, j)]['W'] = 0
        
        self.start_pos = [0, 0]

        self.cur_pos_y = self.start_pos[0]
        self.cur_pos_x = self.start_pos[1]

        self.grid[self.cur_pos_y][self.cur_pos_x] = 'P'
        
        self.valid_moves = []

        self.finish_pos = [COURSE_LENGTH_Y-1, COURSE_LENGTH_X-1]

        self.penalty = -1

        self.reward = 0

        self.trajectories = pd.DataFrame(columns=['state', 'action', 'reward'])

        self.y_moves = {'W' : -1, 'S' : 1}
        self.x_moves = {'D' : 1, 'A' : -1}
    
    def perform_move(self):
        if [self.cur_pos_y, self.cur_pos_x] == self.finish_pos:
            return 1
        elif self.limit == 0:
            return 0

        self.grid[self.cur_pos_y][self.cur_pos_x] = 0

        move = self.policy()
        
        self.trajectories.loc[len(self.trajectories)] = [(self.cur_pos_y, self.cur_pos_x), move, self.penalty]

        self.cur_pos_y += self.y_moves.get(move, 0)
        self.cur_pos_x += self.x_moves.get(move, 0)

        self.grid[self.cur_pos_y][self.cur_pos_x] = 'P'

        self.limit -= 1
        self.reward += self.penalty

        #self.display_grid()
        #print(move)
        #sleep(1)
        return self.perform_move()
    
    def display_grid(self):
        for row in self.grid:
            print(row)
        print('\n')

    def policy(self):
        avg_rewards_for_state_action = self.state_action_average_reward[(self.cur_pos_y, self.cur_pos_x)]

        moves = list(avg_rewards_for_state_action.keys())
        moves_q_scores = list(avg_rewards_for_state_action.values())

        max_reward_move = max(avg_rewards_for_state_action, key=avg_rewards_for_state_action.get)

        if self.epsilon == 0:
            return max_reward_move
        
        elif len(avg_rewards_for_state_action) == 1:
            return moves[0]

        elif all(x == 0 for x in moves_q_scores):
            return np.random.choice(moves)
        
        move_probs_dict = {}

        move_probs_dict[max_reward_move] = 1 - self.epsilon

        moves_besides_max = len(moves) - 1

        for move in moves:
            if move != max_reward_move:
                move_probs_dict[move] = self.epsilon / moves_besides_max

        move_probs = list(move_probs.values())

        return np.random.choice(moves, p = move_probs)