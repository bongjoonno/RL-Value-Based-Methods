# normal imports
from imports import tqdm

# all course_lengths
from train_test import train_test

def test_learning_methods(learning_methods: list[str], course_dims: list[int, int]):
    method_accuracies = {}

    for method in tqdm(learning_methods):
        current_method_accuracies = []
        for course_length in tqdm(course_dims):
            accuracy = train_test(course_length[0], course_length[1], method, display_episode_path = False)
            current_method_accuracies.append(accuracy)
        method_accuracies[method] = current_method_accuracies

    return method_accuracies