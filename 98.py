arr = np.array([[1,2,3], [4,5,6]])
row_mean = arr.mean(axis=1)
column_mean = arr.mean(axis=0)
print('Row mean:', row_mean)
print('Column mean:', column_mean)

