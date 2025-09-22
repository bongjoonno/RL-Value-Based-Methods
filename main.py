# utils
from utils.generate_q_table import gen_q_table

# training
from train import train

# testing
from test import test

#constants
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TESTING_TRIAL_LIMIT, EPOCHS, EPSILON

def main():
    q_scores = gen_q_table(COURSE_LENGTH_Y, COURSE_LENGTH_X)

    finished_params = train(epochs = EPOCHS, q_table = q_scores, method = 'sarsa', epsilon = EPSILON)
    
    accuracy = test(finished_params, TESTING_TRIAL_LIMIT)

    return accuracy


if __name__ == '__main__':
    print(main())