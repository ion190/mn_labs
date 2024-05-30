import numpy as np

A = [
    ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    ['Alice', 0, 1, 1, 0, 0, 0, 0, 0],
    ['Bob', 1, 0, 1, 0, 0, 0, 0, 0],
    ['Charlie', 1, 1, 0, 1, 0, 0, 0, 0],
    ['David', 0, 0, 1, 0, 1, 0, 0, 0],
    ['Eve', 0, 0, 0, 1, 0, 1, 0, 0],
    ['Frank', 0, 0, 0, 0, 1, 0, 1, 0],
    ['Grace', 0, 0, 0, 0, 0, 1, 0, 1],
    ['Hannah', 0, 0, 0, 0, 0, 0, 1, 0]
]

# extract the connectivity matrix from A
# convert it to array of floats
connectivity_matrix = np.array([row[1:] for row in A[1:]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(connectivity_matrix)

# find dominant eigenvalue and its corresponding eigenvector
dominant_index = np.argmax(eigenvalues)
dominant_eigenvalue = eigenvalues[dominant_index]
dominant_eigenvector = eigenvectors[:, dominant_index]

# normalize dominant eigenvector (scaling by dividing it to its max value)
dominant_eigenvector = dominant_eigenvector / np.max(dominant_eigenvector)

print(f"The largest eigenvalue of the matrix λ = {dominant_eigenvalue:.5f}")
print("Its corresponding eigenvector z =")
for value in dominant_eigenvector:
    print(f"{value:.6f}")

# find most influential individual
individuals = A[0]
most_influential_index = np.argmax(dominant_eigenvector)
most_influential_individual = individuals[most_influential_index]
print(f"\nThe most influential individual is {most_influential_individual} (pos. {most_influential_index + 1})")