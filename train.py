# normal imports
from imports import time

# board
from board import Board

# learning methods
from learning_methods.monte_carlo import monte_carlo
from learning_methods.q_learning import q_learning
from learning_methods.sarsa import sarsa
from learning_methods.expected_sarsa import expected_sarsa

# constants
from constants import EPSILON, LEARNING_METHODS

# custom errors
from custom_errors import NonexistentLearningMethod

def train(course_length_y, course_length_x, train_trial_limit, epochs, q_table: dict, method: str, epsilon = EPSILON):
    learning_methods_functions = [monte_carlo, q_learning, sarsa, expected_sarsa]
    learning_methods_map = {LEARNING_METHODS[i]:learning_methods_functions[i] for i in range(len(LEARNING_METHODS))}
    
    chosen_learning_method = learning_methods_map.get(method, None)

    if chosen_learning_method is None:
        raise NonexistentLearningMethod()
    
    for _ in range(epochs):
        board = Board(course_length_y, course_length_x, q_table = q_table, epsilon = epsilon, randomized=True)

        start_training_time = time.monotonic()

        chosen_learning_method(board, train_trial_limit = train_trial_limit)

        total_training_time = time.monotonic() - start_training_time

        initialization_to_training_time_ratio = board.init_total_time / total_training_time
        #print(initialization_to_training_time_ratio)
        
        epsilon = max(0.01, epsilon * 0.999)
        q_table = board.q_table

    return q_table