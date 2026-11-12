# 65. Replace even values with 0 using boolean indexing.
# Beginner Answer

arr = np.array([1, 2, 3, 4, 6, 7])
arr[arr % 2 == 0] = 0
print(arr)

