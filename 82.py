# 82. Solve a system of linear equations using np.linalg.solve().
# Beginner Answer

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print(x)

