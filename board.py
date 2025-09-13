from imports import choice

class Board:
    def __init__(self, limit=5):
        self.limit = limit

        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        
        self.cur_pos = 0
        
        self.finish_pos = len(self.grid)

        self.reward = 0
    
    def get_valid_moves(self):
        self.valid_moves = [1]
        
        if self.cur_pos > 0:
            self.valid_moves.append(-1)
        
    
    def perform_random_move(self):
        if self.cur_pos == self.finish_pos:
            return 'Reached end!', self.reward
        elif self.limit == 0:
            return f"Ran out of trials", self.reward

        self.grid[self.cur_pos] = 0
        
        self.get_valid_moves()

        random_chosen_move = choice(self.valid_moves)

        self.cur_pos += random_chosen_move

        self.grid[self.cur_pos] = 'P'

        self.display_grid()
    
    def display_grid(self):
        print(self.grid)