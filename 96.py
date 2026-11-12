# 96. Replace NaN values with the mean of the array.
# Beginner Answer

arr = np.array([10, np.nan, 20, 30, np.nan])
mean = np.nanmean(arr)
arr[np.isnan(arr)] = mean
print(arr)

