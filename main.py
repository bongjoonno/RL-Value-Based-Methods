from constants import LEARNING_METHODS, TEMPORAL_DIFFERENCE_LEARNING_METHODS

from test_learning_methods import test_learning_methods
from generate_course_dims import generate_course_dims
from get_dimensions_input import get_dimensions_input

def main(learning_methods, course_max_y, course_max_x):
   #course_dims = generate_course_dims(course_max_y, course_max_x)
    methods_perfect_accuracy_dict = test_learning_methods(learning_methods, [[18, 18]])

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':
    x, y = get_dimensions_input()
    methods_accuracy_percentage_dict = main(['q-learning'], 50, 50)
    print(methods_accuracy_percentage_dict)
    
    # 18 x 18 : 1