from math import sqrt

def complex_numbers(a, b):
    C = complex(*a)
    D = complex(*b)
    
    add = C + D
    sub = C - D
    mul = C * D
    div = C / D
    mod_C = sqrt(C.real**2 + C.imag**2)
    mod_D = sqrt(D.real**2 + D.imag**2)
    
    return add, sub, mul, div, f"{mod_C:.2f}{'+' if C.imag >= 0 else ''}{C.imag:.2f}i", f"{mod_D:.2f}{'+' if D.imag >= 0 else ''}{D.imag:.2f}i"