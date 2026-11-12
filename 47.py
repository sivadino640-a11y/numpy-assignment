# 47. Find all numbers divisible by 5.
# Beginner Answer

arr = np.array([10, 12, 15, 22, 25, 31])
print(arr[arr % 5 == 0])

