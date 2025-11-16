def generate_course_dims(y_max_val: int, x_max_val: int) -> list[tuple[int, int]]:
    return [(y, x) for y in range(1, y_max_val + 1) for x in range(2, x_max_val + 1)]