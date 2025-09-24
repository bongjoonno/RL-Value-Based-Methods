from train_test import train_test

def test_different_course_lengths(y_max, x_max, method, display_episode_path):
    accuracies = []
    for y in range(1, y_max):
        for x in range(2, x_max):
            accuracy = train_test(y, x, method, display_episode_path = display_episode_path)
            accuracies.append(accuracy)
    return accuracies