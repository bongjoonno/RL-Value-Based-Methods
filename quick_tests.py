from constants import LEARNING_METHODS_LIST
from test_learning_methods import test_learning_methods
from imports import sys, time

res = test_learning_methods(['Expected Sarsa'], 3, 3)

print(res)