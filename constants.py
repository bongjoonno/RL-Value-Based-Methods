# course-related
course_length_y = 5
course_length_x = 3

TRAIN_FACTOR = 3
TRAINING_TRIAL_LIMIT = ((course_length_y - 1) + (course_length_x - 1)) * TRAIN_FACTOR
TESTING_TRIAL_LIMIT = (course_length_y - 1) + (course_length_x - 1)

# hyper-parameters
EPOCHS = 20_000
ALPHA = 0.1
EPSILON = 1
GAMMA = 0.9

# learning-methods
LEARNING_METHODS = ['monte-carlo', 'q-learning', 'sarsa', 'expected-sarsa']