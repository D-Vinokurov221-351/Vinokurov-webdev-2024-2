

cube = lambda n: cube(n-1) * n if n > 0 else 1 

def fibonacci(n):
    if n == 0:
        return 1
    else:
        return fibonacci(n-1) * n 
    
def fibonacci_it(n):
    i = 2
    ans = 1
    while i <= n:
        ans *= i
        i += 1
    return ans

if __name__ == '__main__':
    import timeit
    n = int(input())
    print(cube(n), timeit.timeit('cube(995)', number=10000, globals=globals()))
    print(fibonacci(n),timeit.timeit('fibonacci(995)', number=10000, globals=globals()))
    print(fibonacci_it(n),timeit.timeit('fibonacci_it(995)', number=10000, globals=globals()))


#функции cube и fibonacci приблизительно равны, но все же работают медленнее чем fibonacci_it