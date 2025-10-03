from constants import MAX_COURSE_LENGTH, LEARNING_METHODS_SET

def get_dimensions_input():
    error_message = "Please enter a number between {} and {}"
    
    minimum_height = 1
    minimum_width = 2
    
    y = input_validation("Enter how tall you want the course to be: ", error_message.format(minimum_height, MAX_COURSE_LENGTH), minimum_dimension = minimum_height)
    x = input_validation("Enter how wide you want the course to be: ", error_message.format(minimum_width, MAX_COURSE_LENGTH), minimum_dimension = minimum_width)
    
    return (y, x)


def input_validation(prompt_message, error_message, minimum_dimension):
    while True:
        try:
            num = int(input(prompt_message))
            
            if num < minimum_dimension or num > MAX_COURSE_LENGTH:
                print(error_message)
                continue
            else:
                break
        except ValueError:
            print(error_message)
            continue
    print("\n")
    return num

def get_learning_methods():
    print("Choose from a Learning Method")
    print("1. Monte Carlo")
    print("2. Q-Learning")
    print("3. Sarsa")
    print("4. Expected-Sarsa")
    print('\n')
    
    learning_method = ""
    
    while learning_method not in LEARNING_METHODS_SET:
        learning_method = input("Learning Method: ")
    
    return learning_method