# normal imports
from imports import time, tqdm

# board
from board import Board

# learning methods
from learning_methods.monte_carlo import monte_carlo
from learning_methods.q_learning import q_learning
from learning_methods.sarsa import sarsa
from learning_methods.expected_sarsa import expected_sarsa

# constants
from constants import EPSILON, LEARNING_METHODS_LIST

# custom errors
from custom_errors import NonexistentLearningMethod

def train(course_length_y, course_length_x, train_trial_limit, epochs, q_table: dict, method: str, epsilon = EPSILON):
    learning_methods_functions = [monte_carlo, q_learning, sarsa, expected_sarsa]
    learning_methods_map = {learning_method: function for learning_method, function in zip(LEARNING_METHODS_LIST, learning_methods_functions)}
    
    chosen_learning_method = learning_methods_map.get(method, None)

    if chosen_learning_method is None:
        raise NonexistentLearningMethod()
    
    print('\n')
    board = Board(epochs, course_length_y, course_length_x, q_table = q_table, epsilon = epsilon, randomized=True)
    
    while True:
        outcome = chosen_learning_method(board, train_trial_limit = train_trial_limit)
        
        if outcome == 'episode ended':
            board = Board(course_length_y, course_length_x, q_table = q_table, epsilon = epsilon, randomized=True)
        elif outcome == 'training ended':
            break
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table
        epochs -= 1

    return q_table