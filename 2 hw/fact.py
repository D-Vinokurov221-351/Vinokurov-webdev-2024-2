def fact_it(n: int):
    ans = 1
    while (n > 1):
        ans *= n
        n -= 1
    return ans


def fact_rec(n: int):
    from time import time
    start = time()
    return n * fact_rec(n - 1) if n > 1 else 1

if __name__ == '__main__':
    from time import time
    n = 1050
    start = time()
    print (fact_it(n))
    print (time() - start)
    start = time()
    print (fact_rec(n))
    print (time() - start)

    # Итог: итерационная функция немного быстрее, но при этом может просчитать числа большие, чем рекурсивная, ведь не перенагружает стэк так быстро

