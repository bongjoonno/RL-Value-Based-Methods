dic = {'monte-carlo': [True, True, True, True, True, True]}

for method, accuracy in dic.items():
    print(method, sum(accuracy) / len(accuracy))