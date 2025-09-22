class NonexistentLearningMethod(Exception):
    def __init__(self):
        super().__init__("Invalid learning method\nPlease pick 'monte carlo', 'q-learning', or 'sarsa'")