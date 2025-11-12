from src.rl_path_finder.imports import np

class Board:
    epsilon = 1
    y_step_mappings = {'W' : -1, 'S' : 1}
    x_step_mappings = {'D' : 1, 'A' : -1}
    penalty = -1

    q_table: dict[tuple[int, int], dict[str, float]]

    course_length_y: int
    course_length_x: int
    trial_limit: int

    def __init__(self, randomized: bool = True) -> None:
        
        self.grid = [[0 for i in range(Board.course_length_x)] for j in range(self.course_length_y)]
        self.grid[-1][-1] = 1
        

        if randomized:
            try:
                self.agent_position_y = np.random.randint(0, Board.course_length_y-1)
            except ValueError:
                self.agent_position_y = 0
            
            self.agent_position_x = np.random.randint(0, Board.course_length_x-1)
        
        else: 
            self.agent_position_y, self.agent_position_x = 0, 0
        
        self.finish_position = (Board.course_length_y-1, Board.course_length_x-1)

        self.grid[self.agent_position_y][self.agent_position_x] = 'P'

        self.trajectories: dict[str, list] = {'state' : [], 'action' : [], 'reward' : []}

        self.chosen_action: str | None = None
        
        self.move_number: int = 0

        self.current_state_q_table: dict[str, float]

        self.max_reward_move_for_state: str | None = None

        self.current_moves_probabilities: np.ndarray | list[float]

        self.current_state_q_scores: np.ndarray

    def perform_move(self) -> str:  
        if self.move_number == self.trial_limit:
            return 'Ran out of trials'
        
        self.grid[self.agent_position_y][self.agent_position_x] = 0

        self.get_next_move()

        self.log_trajectory()

        self.previous_state = (self.agent_position_y, self.agent_position_x)
        self.update_cur_position()
        
        self.move_number += 1
        
        if (self.agent_position_y, self.agent_position_x) == self.finish_position:
            return 'finished course'
        else: 
            return 'continue'
    
    def log_trajectory(self) -> None:
        self.trajectories['state'].append((self.agent_position_y, self.agent_position_x))
        self.trajectories['action'].append(self.chosen_action)
        self.trajectories['reward'].append(Board.penalty)

    def update_cur_position(self) -> None:
        self.agent_position_y += Board.y_step_mappings.get(self.chosen_action, 0)
        self.agent_position_x += Board.x_step_mappings.get(self.chosen_action, 0)
        self.grid[self.agent_position_y][self.agent_position_x] = 'P'

    def display_grid(self) -> None:
        for row in self.grid:
            print(row)

    def update_current_state_q_table(self) -> None:
        self.current_state_q_table = Board.q_table[(self.agent_position_y, self.agent_position_x)]
        self.current_state_q_scores = np.array(list(self.current_state_q_table.values()))
    
    def update_max_reward_move(self) -> None:
        self.max_reward_move_for_state = max(self.current_state_q_table, key = self.current_state_q_table.get)

    def update_available_moves(self) -> None:
        self.available_moves = list(self.current_state_q_table.keys())

    def policy(self) -> None:
        self.current_moves_probabilities =  []

        random_move_prob = self.epsilon / len(self.available_moves)

        for move in self.available_moves:
            if move == self.max_reward_move_for_state:
                self.current_moves_probabilities.append(1 - self.epsilon + random_move_prob)
            else:
                self.current_moves_probabilities.append(random_move_prob)
        
        self.current_moves_probabilities = np.array(self.current_moves_probabilities)

    def get_next_move_prep(self) -> None:
        self.update_current_state_q_table()
        self.update_max_reward_move()
        self.update_available_moves()

    def get_next_move(self) -> None:
        self.get_next_move_prep()
        
        if self.epsilon == 0:
            self.chosen_action = self.max_reward_move_for_state
        
        elif self.epsilon == 1:
            self.chosen_action = np.random.choice(self.available_moves)
        
        elif len(self.available_moves) == 1:
            self.chosen_action = self.available_moves[0]

        elif all(x == 0 for x in self.current_state_q_scores):
            self.chosen_action = np.random.choice(self.available_moves)

        self.policy()

        self.chosen_action = np.random.choice(self.available_moves, p = self.current_moves_probabilities)