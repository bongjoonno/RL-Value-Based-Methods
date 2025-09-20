from board import Board

# learning methods
from learning_methods.monte_carlo import monte_carlo
from learning_methods.q_learning import q_learning
from learning_methods.sarsa import sarsa


# constants
from constants import EPSILON

def train(epochs, q_scores: dict, method: str, epsilon = EPSILON):
    for _ in range(epochs):
        board = Board(state_action_average_reward = q_scores, epsilon = epsilon, randomized=True)

        if method == 'monte carlo':
            monte_carlo(board = board)
        elif method == 'q learning': 
            q_learning(board = board)
        elif method == 'sarsa':
            sarsa(board = board)
        else:
            return "Invalid learning method\n Please pick 'monte carlo', 'q learning', or 'sarsa'"
        epsilon = max(0.01, epsilon * 0.999)
        q_scores = board.state_action_average_reward

    return q_scores