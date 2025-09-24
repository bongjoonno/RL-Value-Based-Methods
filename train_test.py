# utils
from utils.generate_q_table import gen_q_table

# training
from train import train

# testing
from agent_accuracy import has_perfect_accuracy

def train_test(
    course_length_y: int, 
    course_length_x: int, 
    method: str, 
    epochs:int , 
    epsilon: float, 
    testing_trial_limit: int, 
    display_episode_path: bool
) -> bool:
    
    q_scores = gen_q_table(course_length_y, course_length_x)

    finished_q_scores = train(course_length_y, course_length_x, epochs = epochs, q_table = q_scores, method = method, epsilon = epsilon)
    
    accuracy = has_perfect_accuracy(course_length_y, course_length_x, finished_q_scores, testing_trial_limit, display_episode_path = display_episode_path)

    return accuracy


if __name__ == '__main__':
    has_perfect_accuracy = train_test()
    print(has_perfect_accuracy)