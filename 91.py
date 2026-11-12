# 91. Find the row with the highest sum in a 2D array.
# Beginner Answer

arr = np.array([[1,2,3], [10,20,30], [4,5,6]])
row_sums = arr.sum(axis=1)
index = np.argmax(row_sums)
print(index)
print(arr[index])

