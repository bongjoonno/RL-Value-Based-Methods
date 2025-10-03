# normal imports
from imports import tqdm

# all course_lengths
from train_test import train_test

def test_learning_methods(learning_methods: list[str], course_y_dim, course_x_dim):
    method_accuracies = {}

    print("\ntraining...")
    for method in learning_methods:
        current_method_accuracies = []
        accuracy = train_test(course_y_dim, course_x_dim, method, display_episode_path = False)
        current_method_accuracies.append(accuracy)
        method_accuracies[method] = current_method_accuracies

    return method_accuracies