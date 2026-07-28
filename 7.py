def example_7(n: int):
    if n <= 1:
        return 1

    # Each call creates TWO new calls
    return example_7(n - 1) + example_7(n - 1)