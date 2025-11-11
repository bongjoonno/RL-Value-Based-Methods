from src.rl_path_finder.utils.generate_q_table import gen_q_table
from src.rl_path_finder.model import Board, train, has_perfect_accuracy
from src.rl_path_finder.constants import TRAIN_FACTOR, EPOCHS, EPSILON

def train_test(
    course_length_y: int, 
    course_length_x: int, 
    method: str, 
    display_episode_path: bool
) -> bool:

    testing_trial_limit = (course_length_y - 1) + (course_length_x - 1)
    training_trial_limit = int((course_length_y * course_length_x)** TRAIN_FACTOR)
    
    q_table = gen_q_table(course_length_y, course_length_x)

    Board.course_length_y = course_length_y
    Board.course_length_x = course_length_x
    Board.q_table = q_table
    Board.trial_limit = training_trial_limit

    finished_q_scores = train(epochs = EPOCHS, method = method)
    
    accuracy = has_perfect_accuracy(testing_trial_limit, display_episode_path)

    return accuracy