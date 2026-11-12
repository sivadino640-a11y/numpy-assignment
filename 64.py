# 64. Find all odd values using boolean indexing.
# Beginner Answer

arr = np.array([1, 2, 3, 4, 6, 7])
print(arr[arr % 2 != 0])

