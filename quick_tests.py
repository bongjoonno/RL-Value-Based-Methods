def add_2(x):
    print('called')
    return x + 2

y = 5
x = {'yes' : add_2}

chosen_func = x['yes']

print(chosen_func(y))