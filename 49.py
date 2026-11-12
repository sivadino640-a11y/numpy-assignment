# 49. Replace all values greater than 100 with 100.
# Beginner Answer

arr = np.array([50, 120, 80, 150])
arr[arr > 100] = 100
print(arr)

