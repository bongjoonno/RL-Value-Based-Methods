# utils
from utils.generate_q_score_table import gen_q_score_table

# training
from train import train

# testing
from test import test

#constants
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TESTING_TRIAL_LIMIT, EPSILON

def main():
    epochs = 30_000

    q_scores = gen_q_score_table(COURSE_LENGTH_Y, COURSE_LENGTH_X)

    finished_params = train(epochs = epochs, q_scores = q_scores, method = 'sarsa', epsilon = EPSILON)
    
    accuracy = test(finished_params, TESTING_TRIAL_LIMIT)

    return accuracy


if __name__ == '__main__':
    print(main())