def add(x, y):
    return x + y



def multiply(func: add):
    print(add) * 2


print(multiply(add(3, 4)))