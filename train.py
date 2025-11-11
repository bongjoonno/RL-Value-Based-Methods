# board
from board import Board

# learning methods
from learning_methods.monte_carlo import monte_carlo_train
from learning_methods.q_learning import q_learning_train
from learning_methods.sarsa import sarsa_train
from learning_methods.expected_sarsa import expected_sarsa_train

# constants
from constants import EPSILON, LEARNING_METHODS_LIST

# custom errors
from custom_errors import NonexistentLearningMethod

def train(course_length_y, course_length_x, train_trial_limit, epochs, q_table: dict, method: str, epsilon = EPSILON):
    learning_methods_functions = [monte_carlo_train, q_learning_train, sarsa_train, expected_sarsa_train]
    learning_methods_map = {learning_method: function for learning_method, function in zip(LEARNING_METHODS_LIST, learning_methods_functions)}
    
    chosen_learning_method = learning_methods_map.get(method, None)

    if chosen_learning_method is None:
        raise ValueError("Please pick from Monte Carlo, Q-Learning, Sarsa, or Expected Sarsa")
    
    print('\n')
    
    q_table = chosen_learning_method(course_length_y, course_length_x, epochs, q_table, train_trial_limit = train_trial_limit, epsilon = epsilon)
    
    return q_table