from train_test import train_test
from get_inputs import get_dimensions_input, get_learning_methods
from visuals import welcome_message
from imports import time

def main(learning_method, course_length_y, course_length_x):
    has_perfect_accuracy = train_test(course_length_y, course_length_x, learning_method, display_episode_path = True)

    return "\nPerfect path found!" if has_perfect_accuracy else "\nPerfect path not found..."

if __name__ == '__main__':
    welcome_message()
    
    continue_playing = 'y'
    
    while continue_playing.lower() == 'y':
        y, x = get_dimensions_input()
        learning_method = get_learning_methods()
        methods_accuracy_percentage_dict = main(learning_method, y, x)
        print(methods_accuracy_percentage_dict)
        continue_playing = input('\nWould you like to play again??!! (Y): ')
        print('\n')
    
    print('okayyy byyeee!\n')
    time.sleep(1)