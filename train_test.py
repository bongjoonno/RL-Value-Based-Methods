# utils
from utils.generate_q_table import gen_q_table

# training
from train import train

# testing
from agent_accuracy import has_perfect_accuracy

# constants
from constants import TRAIN_FACTOR, EPOCHS, EPSILON

def train_test(
    course_length_y: int, 
    course_length_x: int, 
    method: str, 
    display_episode_path: bool
) -> bool:

    testing_trial_limit = ((course_length_y - 1) + (course_length_x - 1))
    training_trial_limit = TRAIN_FACTOR * course_length_y * course_length_x
    
    q_scores = gen_q_table(course_length_y, course_length_x)

    finished_q_scores = train(course_length_y, course_length_x, training_trial_limit, epochs = EPOCHS, q_table = q_scores, method = method, epsilon = EPSILON)
    
    accuracy = has_perfect_accuracy(course_length_y, course_length_x, finished_q_scores, testing_trial_limit, display_episode_path)

    return accuracy