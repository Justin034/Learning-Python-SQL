def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError('Impossible')
    return x/y