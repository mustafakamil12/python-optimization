import cProfile

def f():
    print('Hello World!')

cProfile.run('f()')