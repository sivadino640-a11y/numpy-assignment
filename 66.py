# 66. Replace values below the mean with the mean.
# Beginner Answer

arr = np.array([10, 20, 30, 40])
mean = arr.mean()
arr[arr < mean] = mean
print(arr)

