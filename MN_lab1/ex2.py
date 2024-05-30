import math

def f(x):
    return x**3 + 2*x**2 + 10*x - 20

def mullers_method(x0, x1, x2, tol):
    max_iterations = 1000
    for _ in range(max_iterations):
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        b = delta2 + h2 * d
        D = math.sqrt(b**2 - 4 * f(x2) * d) if b**2 - 4 * f(x2) * d >= 0 else math.sqrt(-(b**2 - 4 * f(x2) * d)) * 1j
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        
        h = -2 * f(x2) / E
        x3 = x2 + h
        if abs(h) < tol:
            return x3.real
        
        x0 = x1
        x1 = x2
        x2 = x3
        
    print("Method did not converge")
    return None

x0 = 0
x1 = 1
x2 = 2
tolerance = 1e-8

root = mullers_method(x0, x1, x2, tolerance)
if root is not None:
    print(f"The root found is: {root:.8f}")
else:
    print("No root found or method did not converge.")