from imports import cProfile, pstats

from constants import LEARNING_METHODS

from test_learning_methods import test_learning_methods


def main():
    methods_perfect_accuracy_dict = test_learning_methods(LEARNING_METHODS, 2, 3)

    methods_accuracy_percentage_dict = {}

    for method, accuracy in methods_perfect_accuracy_dict.items():
        methods_accuracy_percentage_dict[method] =  sum(accuracy) / len(accuracy)

    return methods_accuracy_percentage_dict

if __name__ == '__main__':
    profiler = cProfile.Profile()
    
    profiler.enable()
    methods_accuracy_percentage_dict = main()
    profiler.disable()
    
    #for method, accuracy in methods_accuracy_percentage_dict.items():
        #print(f"{method} accuracy: {accuracy*100:.2f}%")
    

    stats = pstats.Stats(profiler).sort_stats("cumulative")
    stats.print_stats()
