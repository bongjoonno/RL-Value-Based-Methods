# normal imports
from imports import np

# constants
from constants import LEARNING_METHODS

# all course_lengths
from test_different_course_lengths import test_different_course_lengths

def test_learning_methods(methods: list[str]):
    method_accuracies = {method:None for method in methods}

    for method in methods:
        accuracies = test_different_course_lengths(4, 4, method, display_episode_path = False)
        method_accuracies[method] = accuracies

    return method_accuracies

if __name__ == '__main__':
    learning_methods = LEARNING_METHODS

    average_accuracy = test_learning_methods(learning_methods)
    print(average_accuracy)