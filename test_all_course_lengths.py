from test_learning_methods import test_learning_methods
from constants import LEARNING_METHODS


def test_all_course_lengths(learning_methods: list[str]):
    areas_accuracies = {}

    for y in range(10):
        for x in range(10):
            area = x * y
            accuracy = test_learning_methods(learning_methods)
            areas_accuracies[area] = accuracy