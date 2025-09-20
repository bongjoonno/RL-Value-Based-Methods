# board
from board import Board

# utils
from utils.generate_q_score_table import gen_q_score_table
from utils.save_parameters import save_parameters_to_pkl

# training
from train import train

# testing
from test import test

#constants
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TRAINING_TRIAL_LIMIT, TESTING_TRIAL_LIMIT, ALPHA, EPSILON, GAMMA

def main():
    epochs = 20_000

    q_scores = gen_q_score_table(COURSE_LENGTH_Y, COURSE_LENGTH_X)

    finished_params = train(epochs = epochs, q_scores = q_scores, method = 'q learning', epsilon = EPSILON)
    
    accuracy = test(finished_params, TESTING_TRIAL_LIMIT)

    return accuracy


if __name__ == '__main__':
    print(main())