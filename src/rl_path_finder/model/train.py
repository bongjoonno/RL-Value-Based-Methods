# board
from src.rl_path_finder.model import Board

# learning methods
from src.rl_path_finder.learning_methods import monte_carlo_train, q_learning_train, sarsa_train, expected_sarsa_train

# constants
from src.rl_path_finder.constants import EPSILON, LEARNING_METHODS_LIST

def train(epochs, q_table: dict, method: str, epsilon = EPSILON):
    learning_methods_functions = [monte_carlo_train, q_learning_train, sarsa_train, expected_sarsa_train]
    learning_methods_map = {learning_method: function for learning_method, function in zip(LEARNING_METHODS_LIST, learning_methods_functions)}
    
    chosen_learning_method = learning_methods_map.get(method, None)

    if chosen_learning_method is None:
        raise ValueError("Please pick from Monte Carlo, Q-Learning, Sarsa, or Expected Sarsa")
    
    print('\n')
    
    q_table = chosen_learning_method(course_length_y, course_length_x, epochs, q_table, train_trial_limit = train_trial_limit, epsilon = epsilon)
    
    return q_table