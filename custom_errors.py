from constants import LEARNING_METHODS_LIST

class NonexistentLearningMethod(Exception):
    def __init__(self):
        super().__init__("Invalid learning method\n"
                         f"Please select from {LEARNING_METHODS_LIST}")