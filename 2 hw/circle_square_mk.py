import random

def circle_square_mk(r, n):
    inside = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            inside += 1
    
    square = (inside / n) * (4 * r ** 2)
    
    return square