# normal imports
from imports import np

# constants
from constants import course_length_y, course_length_x, TESTING_TRIAL_LIMIT, EPOCHS, EPSILON, LEARNING_METHODS

# train_test
from train_test import train_test

def test_learning_methods(methods: list[str]):
    method_accuracies = {method:[] for method in methods}

    for method in methods:
        for y in range(1, 2):
            for x in range(3, 4):
                accuracy = train_test(y, x, method, EPOCHS, EPSILON, TESTING_TRIAL_LIMIT, display_episode_path = False)
            method_accuracies[method].append(accuracy)

    return method_accuracies

if __name__ == '__main__':
    learning_methods = LEARNING_METHODS

    average_accuracy = test_learning_methods(learning_methods)
    print(average_accuracy)