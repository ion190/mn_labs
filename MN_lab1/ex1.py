import math

def f(x):
    return math.exp(x) - x**2

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No root")
        return None
    a_n = a
    b_n = b
    while (b_n - a_n) / 2.0 > tol:
        midpoint = (a_n + b_n) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a_n) * f(midpoint) < 0:
            b_n = midpoint
        else:
            a_n = midpoint
    return (a_n + b_n) / 2.0

a = -2
b = 0
tolerance = 1e-8
root = bisection_method(a, b, tolerance)
if root is not None:
    print(f"The root found is: {root:.8f}")
else:
    print("No root found in the given interval.")