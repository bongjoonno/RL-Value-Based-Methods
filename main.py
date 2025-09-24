from imports import cProfile, pstats

from constants import LEARNING_METHODS

from test_learning_methods import test_learning_methods


def main(y_max, x_max, learning_methods):
    methods_perfect_accuracy_dict = test_learning_methods(learning_methods, y_max, x_max)

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':
    y_max = 3
    x_max = 4

    profiler = cProfile.Profile()
    
    profiler.enable()
    methods_accuracy_percentage_dict = main(y_max, x_max, ['expected-sarsa'])
    profiler.disable()
    
    for method, accuracy in methods_accuracy_percentage_dict.items():
        print(f"{method} accuracy: {accuracy*100:.2f}%")
    

    stats = pstats.Stats(profiler).sort_stats("cumulative")
    #stats.print_stats()
