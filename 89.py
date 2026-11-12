# 89. Find values that occur exactly once.
# Beginner Answer

arr = np.array([1, 2, 2, 3, 4, 4, 5])
values, counts = np.unique(arr, return_counts=True)
print(values[counts == 1])

