from constants import LEARNING_METHODS

from test_learning_methods import test_learning_methods

methods_accuracy_dict = test_learning_methods(LEARNING_METHODS, 10, 10)

for method, accuracy in methods_accuracy_dict.items():
    print(method, sum(accuracy) / len(accuracy))