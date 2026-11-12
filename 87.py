# 87. Find the third-largest value without sorting the entire array.
# Beginner Answer

arr = np.array([10, 50, 30, 80, 20, 60])
third = np.partition(arr, -3)[-3]
print(third)

