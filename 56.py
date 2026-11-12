# 56. Swap the first and last rows of a matrix.
# Beginner Answer

arr = np.array([[1, 2], [3, 4], [5, 6]])
arr[[0, -1]] = arr[[-1, 0]]
print(arr)

