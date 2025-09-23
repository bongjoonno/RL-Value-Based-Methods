# board
from board import Board

# learning methods
from learning_methods.monte_carlo import monte_carlo
from learning_methods.q_learning import q_learning
from learning_methods.sarsa import sarsa
from learning_methods.expected_sarsa import expected_sarsa

# constants
from constants import EPSILON

# custom errors
from custom_errors import NonexistentLearningMethod

def train(epochs, q_table: dict, method: str, epsilon = EPSILON):
    learning_methods_map = {'monte carlo' : monte_carlo,
                            'q-learning' : q_learning,
                            'sarsa' : sarsa,
                            'expected sarsa' : expected_sarsa}
    
    chosen_learning_method = learning_methods_map.get(method, None)

    if chosen_learning_method is None:
        raise NonexistentLearningMethod()
    
    for _ in range(epochs):
        board = Board(q_table = q_table, epsilon = epsilon, randomized=True)

        chosen_learning_method(board)
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table

    return q_table