def fibonacci(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        #  Each call creates TWO!! new calls
        fibonacci_N = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_N