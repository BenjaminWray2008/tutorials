#hint the time complexity is determined by BOTH 'a' and 'b'

def example_2(a: int, b: int):
    for x in range(a):
        for y in range(b):
            print(x, y)