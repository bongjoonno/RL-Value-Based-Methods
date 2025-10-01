def get_dimensions_input():
    error_message = "Please enter a number between 1 and 25"
    y = input_validation("Enter how tall you want the course to be: ", error_message)
    x = input_validation("Enter how wide you want the course to be: ", error_message)
    return (y, x)


def input_validation(prompt_message, error_message):
    while True:
        try:
            print("\n")
            num = int(input(prompt_message))
            
            if num < 1 or num > 15:
                print(error_message)
                continue
            else:
                break
        except ValueError:
            print(error_message)
            continue
    return num

def get_learning_methods():
    