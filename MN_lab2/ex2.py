import numpy as np
import matplotlib.pyplot as plt

dates = np.array(["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05", 
                  "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10", 
                  "2020-01-11", "2020-01-12", "2020-01-13", "2020-01-14", "2020-01-15", 
                  "2020-01-16", "2020-01-17", "2020-01-18", "2020-01-19", "2020-01-20", 
                  "2020-01-21", "2020-01-22", "2020-01-23", "2020-01-24", "2020-01-25", 
                  "2020-01-26", "2020-01-27", "2020-01-28", "2020-01-29", "2020-01-30", 
                  "2020-01-31", "2020-02-01", "2020-02-02", "2020-02-03", "2020-02-04", 
                  "2020-02-05", "2020-02-06", "2020-02-07", "2020-02-08", "2020-02-09", 
                  "2020-02-10", "2020-02-11", "2020-02-12", "2020-02-13", "2020-02-14", 
                  "2020-02-15", "2020-02-16", "2020-02-17", "2020-02-18", "2020-02-19", 
                  "2020-02-20", "2020-02-21", "2020-02-22", "2020-02-23", "2020-02-24", 
                  "2020-02-25", "2020-02-26", "2020-02-27", "2020-02-28", "2020-02-29", 
                  "2020-03-01", "2020-03-02", "2020-03-03", "2020-03-04", "2020-03-05", 
                  "2020-03-06", "2020-03-07", "2020-03-08", "2020-03-09", "2020-03-10", 
                  "2020-03-11", "2020-03-12", "2020-03-13", "2020-03-14", "2020-03-15"])

visitors = np.array([543, 674, 825, 947, 1021, np.nan, 1154, 1215, 1305, np.nan, 1465, 1527, 
                     1612, 1698, 1764, 1827, 1884, 1950, 2037, 2120, 2201, 2298, 2397, 2481, 
                     2578, 2672, np.nan, 2871, 2983, 3089, 3176, 3261, 3338, 3439, 3557, 3681, 
                     3802, 3908, 4012, np.nan, 4227, 4351, 4491, 4619, 4752, 4878, 5011, 5145, 
                     5291, 5425, 5545, 5683, 5815, np.nan, 6072, 6199, 6341, np.nan, 6610, 6752, 
                     np.nan, 7023, 7183, 7324, np.nan, 7602, 7765, 7931, 8105, 8257, 8433, 8615, 
                     8788, 8961, 9149])

def linear_interpolate(x, y, xi):
    x = np.array(x)
    y = np.array(y)
    indices = np.argsort(x)
    x = x[indices]
    y = y[indices]
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

# extract non-NaN data
x = np.array([i for i in range(len(visitors)) if not np.isnan(visitors[i])])
y = np.array([visitors[i] for i in range(len(visitors)) if not np.isnan(visitors[i])])
xi = np.array([i for i in range(len(visitors))])

# do interpolations
linear_interp = linear_interpolate(x, y, xi)
newton_interp = newton_interpolate(x, y, xi)

# replace NaNs with interpolated values
linear_filled = visitors.copy()
newton_filled = visitors.copy()
linear_filled[np.isnan(visitors)] = linear_interp[np.isnan(visitors)]
newton_filled[np.isnan(visitors)] = newton_interp[np.isnan(visitors)]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(xi, visitors, 'o', label='Original Data')
plt.plot(xi, linear_filled, '-', label='Linear Interpolation')
plt.plot(xi, newton_filled, '--', label='Newton Interpolation')
plt.xlabel('Day')
plt.ylabel('Visitors')
plt.legend()
plt.title('Website Visitors Interpolation')
plt.show()
