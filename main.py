from constants import LEARNING_METHODS

from test_learning_methods import test_learning_methods


def main(learning_methods):
    methods_perfect_accuracy_dict = test_learning_methods(learning_methods)

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':

    methods_accuracy_percentage_dict = main(['q-learning'])