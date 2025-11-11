def gen_q_table(course_length_y: int, course_length_x: int) -> dict[tuple[int, int], dict[str, float]]:
    q_scores = {(i, j): {} for i in range(course_length_y) for j in range(course_length_x)}

    for i in range(course_length_y):
        for j in range(course_length_x):
            if j < course_length_x - 1:
                q_scores[(i, j)]['D'] = 0
            if j > 0:
                q_scores[(i, j)]['A'] = 0
            if i < course_length_y - 1:
                q_scores[(i, j)]['S'] = 0
            if i > 0:
                q_scores[(i, j)]['W'] = 0
    
    return q_scores