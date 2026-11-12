# 48. Replace all negative values with 0.
# Beginner Answer

arr = np.array([-3, 5, -1, 8])
arr[arr < 0] = 0
print(arr)

