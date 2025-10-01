from constants import LEARNING_METHODS_LIST
from test_learning_methods import test_learning_methods
from imports import sys, time

#res = test_learning_methods(LEARNING_METHODS_LIST, 10, 10)

#print(res)

lst = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for lt in lst:
    print(lt)

time.sleep(1)
    
for _ in range(len(lst)):
    sys.stdout.write("\033[F")  # move cursor up one line
    sys.stdout.write("\033[K")