def example_one(arr):
    first_item = arr[0]
    print(first_item)


def example_two(arr):
    for item in arr:
        print(item)

    for item in arr:
        print(item * 2)


def example_three(arr):
    total = 0
    for item in arr:
        total += item
    return total


def example_four(arr):
    for i in arr:
        for j in arr:
            print(i, j)


def example_five(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count