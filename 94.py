# 94. Find all values that are above the array's mean.
# Beginner Answer

arr = np.array([10, 20, 30, 40, 50])
mean = arr.mean()
print(arr[arr > mean])

