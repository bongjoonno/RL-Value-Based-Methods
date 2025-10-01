from train_test import train_test
from get_inputs import get_dimensions_input, get_learning_methods

def main(learning_method, course_length_y, course_length_x):
    methods_perfect_accuracy_dict = train_test(course_length_y, course_length_x, learning_method, display_episode_path = True)

    return methods_perfect_accuracy_dict

if __name__ == '__main__':
    y, x = get_dimensions_input()
    learning_method = get_learning_methods()
    methods_accuracy_percentage_dict = main(learning_method, y, x)
    print(methods_accuracy_percentage_dict)