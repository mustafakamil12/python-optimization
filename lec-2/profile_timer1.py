import time

def my_func():
    a = 5 + 4
    b = 4 + 4
    # c = a + b
    # d = c/b
    d = (a + b)/b
    return d

start = time.time()
my_func()
print('Time consumed: {} secs'.format(time.time() - start))