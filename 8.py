#this is an exmaple of an implementaiton of binary search

def example_8(sorted_list: list, target: int):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index

        if sorted_list[mid] == target:
            return mid
        
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1