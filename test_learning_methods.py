# normal imports
from imports import np

# constants
from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X, TESTING_TRIAL_LIMIT, EPOCHS, EPSILON, LEARNING_METHODS

# train_test
from train_test import train_test

def test_learning_methods(methods: list[str]):
    accuracies = []

    for method in methods:
        accuracy = train_test(COURSE_LENGTH_Y, COURSE_LENGTH_X, method, EPOCHS, EPSILON, TESTING_TRIAL_LIMIT)
        accuracies.append(accuracy)

    average_accuracy = np.mean(accuracies)

    return average_accuracy

if __name__ == '__main__':
    average_accuracy = test_learning_methods(LEARNING_METHODS)