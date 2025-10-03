from constants import MAX_COURSE_LENGTH, LEARNING_METHODS_SET

def get_dimensions_input():
    error_message = f"Please enter a number between 1 and {MAX_COURSE_LENGTH}"
    y = input_validation("Enter how tall you want the course to be: ", error_message)
    x = input_validation("Enter how wide you want the course to be: ", error_message)
    return (y, x)


def input_validation(prompt_message, error_message):
    while True:
        try:
            num = int(input(prompt_message))
            
            if num < 1 or num > MAX_COURSE_LENGTH:
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