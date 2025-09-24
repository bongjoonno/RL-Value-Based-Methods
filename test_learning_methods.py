# normal imports
from imports import np

# all course_lengths
from test_different_course_lengths import test_different_course_lengths

def test_learning_methods(methods: list[str], y_max, x_max):
    method_accuracies = {}

    for method in methods:
        accuracies = test_different_course_lengths(y_max, x_max, method, display_episode_path = False)
        method_accuracies[method] = accuracies

    return method_accuracies