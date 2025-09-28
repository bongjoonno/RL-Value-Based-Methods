from constants import LEARNING_METHODS

from test_learning_methods import test_learning_methods
from generate_course_dims import generate_course_dims

def main(learning_methods):
    course_dims = generate_course_dims(3, 3)
    methods_perfect_accuracy_dict = test_learning_methods(learning_methods, course_dims)

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':

    methods_accuracy_percentage_dict = main(['expected-sarsa'])
    print(methods_accuracy_percentage_dict)