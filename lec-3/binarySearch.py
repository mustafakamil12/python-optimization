import bisect
import random
import time

def find_closet(numbers, my_val):
    i = bisect.bisect_left(numbers, my_val)
    j = 0
    if i == len(numbers):
        return i - 1
    elif numbers[i] == my_val:
        return i
    elif i < 0:
        j = i -1
        if numbers[i] - my_val > my_val - numbers [j]:
            return j
    return i

start = time.time()
numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(numbers, new_number)
print(numbers)
closest_index = find_closet(numbers, 500)
print(numbers[closest_index])
print('Time consumed is {} secs'.format(time.time() - start))

