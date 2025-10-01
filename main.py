from constants import LEARNING_METHODS, TEMPORAL_DIFFERENCE_LEARNING_METHODS

from test_learning_methods import test_learning_methods
from generate_course_dims import generate_course_dims
from get_inputs import get_dimensions_input

def main(learning_methods, course_y_dim, course_x_dim):
    methods_perfect_accuracy_dict = test_learning_methods(learning_methods, course_y_dim, course_x_dim)

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':
    y, x = get_dimensions_input()
    learning_methods = get_learning_methods()
    methods_accuracy_percentage_dict = main(['q-learning'], y, x)
    print(methods_accuracy_percentage_dict)