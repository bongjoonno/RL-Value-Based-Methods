# all course_lengths
from src.rl_path_finder.model import train_test

def test_learning_methods(learning_methods: list[str], course_length_y, course_length_x):
    method_accuracies = {}

    print("\ntraining...")
    for method in learning_methods:
        current_method_accuracies = []
        accuracy = train_test(course_length_y, course_length_x, method, display_episode_path = False)
        current_method_accuracies.append(accuracy)
        method_accuracies[method] = current_method_accuracies

    return method_accuracies