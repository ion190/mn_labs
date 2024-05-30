import numpy as np

def parse_equations(equations):
    def f(vars):
        x, y, z = vars
        return np.array([eval(eq) for eq in equations])
    return f

def jacobian(f, x, h=1e-8):
    n = len(x)
    J = np.zeros((n, n))
    f0 = f(x)
    for i in range(n):
        x1 = np.copy(x)
        x1[i] += h
        f1 = f(x1)
        J[:, i] = (f1 - f0) / h
    return J

def newton_raphson(f, x0, tol):
    x = np.array(x0, dtype=float)
    for _ in range(100):
        J = jacobian(f, x)
        f_val = f(x)
        delta = np.linalg.solve(J, -f_val)
        x += delta
        if np.linalg.norm(delta, ord=2) < tol:
            return x
    raise ValueError("Newton-Raphson method did not converge")

equations = []
print("Enter the system of equations (one per line, end with an empty line):")
while True:
    eq = input()
    if eq.strip() == "":
        break
    equations.append(eq.strip())

initial_guesses = input("Enter the initial guesses (comma-separated): ")
x0 = list(map(float, initial_guesses.split(',')))
tol = float(input("Enter the desired tolerance: "))
f = parse_equations(equations)
roots = newton_raphson(f, x0, tol)
print("The roots of the system of equations are:", roots)

# Example:
# x**2 + y**2 + z**2 - 1
# x + y + z - 1
# x**3 - y - z