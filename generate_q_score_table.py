from constants import COURSE_LENGTH_Y, COURSE_LENGTH_X

def gen_q_score_table():
    state_action_average_reward = {(i, j): {} for i in range(COURSE_LENGTH_Y) for j in range(COURSE_LENGTH_X)}

    for i in range(COURSE_LENGTH_Y):
        for j in range(COURSE_LENGTH_X):
            if j < COURSE_LENGTH_X - 1:
                state_action_average_reward[(i, j)]['D'] = 0
            if j > 0:
                state_action_average_reward[(i, j)]['A'] = 0
            if i < COURSE_LENGTH_Y - 1:
                state_action_average_reward[(i, j)]['S'] = 0
            if i > 0:
                state_action_average_reward[(i, j)]['W'] = 0
    
    return state_action_average_reward