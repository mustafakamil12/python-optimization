import random
import time 

def find_closet(numbers, my_val):
    for i, number in enumerate(numbers):
        if number == my_val:
            return i - 1
        elif number < my_val:
            if number < numbers[i+1] and numbers[i+1] < my_val:
                continue
            return i


start = time.time()        
numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    numbers.append(new_number)
    numbers.sort()
    
print(numbers)

closest_index = find_closet(numbers, 500)
print(numbers[closest_index])
print('Time consumed {} secs'.format(time.time() - start))