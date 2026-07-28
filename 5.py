from math import sqrt

def example_5(n: int):
    for x in range(n):
        print(x)

    i = 1
    while i < sqrt(n):
        print(i)
        i += 1

    for i in range(n):
        for j in range(n):
            print(i, j)