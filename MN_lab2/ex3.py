import numpy as np
import matplotlib.pyplot as plt

data_text = """
1, 10
2, 15
3, 25
4, 30
5, 35
6, 40
7, 42
8, 45
9, 48
10, 50
11, 55
12, 58
13, 60
14, 63
15, 65
16, 68
17, 70
18, 75
19, 80
20, 85
21, 90
22, 92
23, 95
24, 98
25, 100
26, 105
27, 110
28, Nan
29, 120
30, 125
31, 130
32, 135
33, 140
34, 145
35, 150
36, Nan
37, 160
38, 165
39, 170
40, Nan
41, 180
42, 185
43, 190
44, Nan
45, 200
46, 205
47, 210
48, Nan
49, 220
50, 225
51, 230
52, 235
53, 240
54, 245
55, 250
56, Nan
57, 260
58, 265
59, 270
60, 275
61, 280
62, 285
63, 290
64, Nan
65, 300
66, 305
67, 310
68, Nan
69, 320
70, 325
71, 330
72, Nan
73, 340
74, 345
75, 350
76, 355
77, 360
78, 365
79, 370
80, Nan
81, 380
82, 385
83, 390
84, 395
85, 400
86, 405
87, 410
88, 415
89, 420
90, 425
91, 430
92, 435
93, 440
94, 445
95, 450
96, 455
97, 460
98, 465
99, 470
100, 475
"""

# parsse
lines = data_text.strip().split('\n')
data = np.array([list(map(lambda x: float('nan') if x.strip() == 'Nan' else float(x.strip()), line.split(','))) for line in lines])

items = data[:, 0]
times = data[:, 1]

# remove NaNs
items_valid = items[~np.isnan(times)]
times_valid = times[~np.isnan(times)]

def lagrange_interpolate(x, y, xi):
    def basis(j, xi):
        b = [(xi - x[m])/(x[j] - x[m]) for m in range(len(x)) if m != j]
        return np.prod(b, axis=0)

    return sum(y[j] * basis(j, xi) for j in range(len(x)))

def piecewise_linear_interpolate(x, y, xi):
    return np.interp(xi, x, y)

def newton_interpolate(x, y, xi):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    
    def newton_poly(xi):
        result = coef[0, 0]
        for i in range(1, n):
            term = coef[0, i]
            for j in range(i):
                term *= (xi - x[j])
            result += term
        return result

    return np.array([newton_poly(xi_i) for xi_i in xi])

def cubic_spline_interpolate(x, y, xi):
    return np.interp(xi, x, y, left=np.nan, right=np.nan, period=None)

def romberg_integration(f, a, b, tol=1e-6):
    R = np.zeros((2, 2))
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))
    
    k = 1
    while True:
        h /= 2
        sum_f = sum(f(a + i*h) for i in range(1, 2**k, 2))
        R[1, 0] = 0.5 * R[0, 0] + h * sum_f
        
        for j in range(1, k+1):
            R[1, j] = R[1, j-1] + (R[1, j-1] - R[0, j-1]) / (4**j - 1)
        
        if abs(R[1, k] - R[0, k-1]) < tol:
            return R[1, k]
        
        R[0, :k+1] = R[1, :k+1]
        k += 1
        R = np.resize(R, (2, k+1))

# predict values
xi = np.linspace(min(items), max(items), 100)
lagrange_interp = lagrange_interpolate(items_valid, times_valid, xi)
linear_interp = piecewise_linear_interpolate(items_valid, times_valid, xi)
newton_interp = newton_interpolate(items_valid, times_valid, xi)
cubic_interp = cubic_spline_interpolate(items_valid, times_valid, xi)

plt.figure(figsize=(10, 5))
plt.plot(items, times, 'o', label='Original Data')
plt.plot(xi, lagrange_interp, '-', label='Lagrange Interpolation')
plt.plot(xi, linear_interp, '-', label='Piecewise Linear Interpolation')
plt.plot(xi, newton_interp, '--', label='Newton Interpolation')
plt.plot(xi, cubic_interp, '--', label='Cubic Spline Interpolation')
plt.xlabel('Number of Items Purchased')
plt.ylabel('Time Spent (minutes)')
plt.legend()
plt.title('Interpolation Methods')
plt.show()

# example function for Romberg Integration
def example_func(x):
    return np.sin(x)

# calculate area
a = 0
b = np.pi
area = romberg_integration(example_func, a, b)
print(f"Area under curve: {area}")