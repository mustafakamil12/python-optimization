my_list = [9, 18, 28, 88, 29, 61, 56, 42, 19, 95]

def linear_search(elem, array):
    for i, item in enumerate(array):
        if item == elem:
            return i
    return -1

print(linear_search(42, my_list))