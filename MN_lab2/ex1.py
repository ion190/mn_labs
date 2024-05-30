import numpy as np
import math

def gauss_legendre_quadrature(func, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5 * (x + 1) * (b - a) + a
    wt = 0.5 * (b - a) * w
    integral = 0.0
    for i in range(n):
        integral += wt[i] * func(t[i])
    
    return integral

def parse_equation(equation):
    def f(t):
        return eval(equation)
    return f

print("Enter the equation of motion to integrate (in terms of variable t):")
equation = input().strip()
func = parse_equation(equation)
a = float(input("Enter the lower bound of the range: "))
b = float(input("Enter the upper bound of the range: "))
tol = float(input("Enter the desired tolerance: "))

n = 2
previous_result = gauss_legendre_quadrature(func, a, b, n)
while True:
    n *= 2
    current_result = gauss_legendre_quadrature(func, a, b, n)
    
    if abs(current_result - previous_result) < tol:
        break
    
    previous_result = current_result
print(f"The approximate value of the integral is: {current_result}")