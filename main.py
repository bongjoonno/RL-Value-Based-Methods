from train_test import train_test
from utils.get_inputs import get_dimensions_input, get_learning_methods
from visuals import welcome_message

def main(learning_method, course_length_y, course_length_x):
    has_perfect_accuracy = train_test(course_length_y, course_length_x, learning_method, display_episode_path = True)

    return "Perfect path found!" if has_perfect_accuracy else "Perfect path not found..."

if __name__ == '__main__':
    welcome_message()
    y, x = get_dimensions_input()
    learning_method = get_learning_methods()
    methods_accuracy_percentage_dict = main(learning_method, y, x)
    print(methods_accuracy_percentage_dict)
    
    # TO DO
    # input validation for x < 2 
    # make into executable
    # only count used epochs