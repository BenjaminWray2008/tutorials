def example_1(n: int):
    for i in range(n):
        for j in range(i):  # Runs up to 'i' NOT 'n'
            print(i, j)