# 93. Find the top 3 values and their indexes.
# Beginner Answer

arr = np.array([10, 80, 30, 60, 90, 40])
indexes = np.argsort(arr)[-3:][::-1]
print('Indexes:', indexes)
print('Values:', arr[indexes])

