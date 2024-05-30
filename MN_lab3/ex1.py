import numpy as np
import matplotlib.pyplot as plt

equations = [
    (2, -1, 4),
    (3, 2, 7),
    (1, 1, 3),
    (4, -1, 1),
    (1, -3, -2)
]

def solve_for_xy(a, b, c):
    A = np.array([[a, b]])
    b = np.array([c])
    solutions, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    return solutions

stone_coordinates = []
for i, (a, b, c) in enumerate(equations):
    solutions = solve_for_xy(a, b, c)
    if solutions.shape[0] == 2:
        x, y = solutions
    else:
        x = solutions[0]
        y = (c - a * x) / b

    stone_coordinates.append((x, y, f'Stone {i + 1}'))

stone_coordinates.sort(key=lambda stone: stone[0])

print("\nOrder of stepping stones:")
for stone in stone_coordinates:
    print(f"{stone[2]}: (x = {stone[0]:.2f}, y = {stone[1]:.2f})")

x_coords = [stone[0] for stone in stone_coordinates]
y_coords = [stone[1] for stone in stone_coordinates]
labels = [stone[2] for stone in stone_coordinates]

plt.figure(figsize=(10, 6))
plt.plot(x_coords, y_coords, 'bo-', markersize=10)
for i, label in enumerate(labels):
    plt.text(x_coords[i], y_coords[i], label, fontsize=12, ha='right')

plt.title('Stepping Stones Path')
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.grid(True)
plt.show()