# normal imports
from imports import pd, sleep, pickle

# board
from board_multi_dimensional import BoardMultiDimensional

# utils
from utils.generate_q_score_table import gen_q_score_table

# learning methods
from learning_methods.monte_carlo import monte_carlo
from learning_methods.q_learning import q_learning
from learning_methods.sarsa import sarsa

# testing
from test import test_multi_dim

#constants
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TRAINING_TRIAL_LIMIT, TESTING_TRIAL_LIMIT, ALPHA, EPSILON, GAMMA

def main():
    epochs = 20_000

    epsilon = EPSILON

    q_scores = gen_q_score_table(COURSE_LENGTH_Y, COURSE_LENGTH_X)

    for _ in range(epochs):
        board = BoardMultiDimensional(state_action_average_reward = q_scores, epsilon = epsilon, randomized=True)

        #monte_carlo(board = board)
        #q_learning(board = board)
        sarsa(board = board)
        
        epsilon = max(0.01, epsilon * 0.999)
        q_scores = board.state_action_average_reward
        #print(epsilon)

    for state, actions in q_scores.items():
        print(state, actions)

    with open('/workspaces/monte-carlo/state_action_average_reward.pkl', 'wb') as f:
        pickle.dump(q_scores, f)
    
    accuracy = test_multi_dim(q_scores, TESTING_TRIAL_LIMIT)

    return accuracy


if __name__ == '__main__':
    print(main())