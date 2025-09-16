from constants import COURSE_LENGTH_X, COURSE_LENGTH_Y
from board_multi_dimensional import BoardMultiDimensional

state_action_average_reward = {(i, j):0 for i in range(COURSE_LENGTH_X) for j in range(COURSE_LENGTH_Y)}

board = BoardMultiDimensional(state_action_average_reward=state_action_average_reward)

board.get_valid_moves()

print(board.valid_moves)