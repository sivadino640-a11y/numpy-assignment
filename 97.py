

arr = np.array([[1, 2], [3, np.nan], [5, 6], [np.nan, 8]])
clean = arr[~np.isnan(arr).any(axis=1)]
print(clean)

