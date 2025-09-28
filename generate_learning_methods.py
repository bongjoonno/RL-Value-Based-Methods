def generate_learning_methods(y_max_val, x_max_val):
    return [[y, x] for y in range(1, y_max_val + 1) for x in range(2, x_max_val + 1)]