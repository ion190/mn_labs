import numpy as np

coordinates = np.array([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
                        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
elevations = np.array([50, 60, np.nan, 70, np.nan, 80,
                       40, np.nan, 45, 55, np.nan, 65,
                       np.nan, 70, np.nan, 80, 90, 100])

def idw_interpolate(x, y, z, xi, yi, p=2):
    # Remove NaN values
    valid_mask = ~np.isnan(z)
    x_valid = x[valid_mask]
    y_valid = y[valid_mask]
    z_valid = z[valid_mask]
    
    weights = 1 / np.sqrt((xi - x_valid)**2 + (yi - y_valid)**2)**p
    return np.sum(weights * z_valid) / np.sum(weights)

# Prepare grid for interpolation
grid_x, grid_y = np.meshgrid(np.arange(0, 6), np.arange(0, 3))
grid_z = np.zeros_like(grid_x, dtype=float)

# IDW interpolation on the grid
for i in range(grid_x.shape[0]):
    for j in range(grid_x.shape[1]):
        if np.isnan(elevations[i * grid_x.shape[1] + j]):
            grid_z[i, j] = idw_interpolate(coordinates[:, 0], coordinates[:, 1], elevations, grid_x[i, j], grid_y[i, j])
        else:
            grid_z[i, j] = elevations[i * grid_x.shape[1] + j]

# Print the grid in a formatted way
print("Interpolated Elevation Grid:")
for i in range(grid_z.shape[0]):
    for j in range(grid_z.shape[1]):
        print(f"{grid_z[i, j]:8.2f}", end=' ')
    print()
