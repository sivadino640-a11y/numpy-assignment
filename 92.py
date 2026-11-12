# 92. Find the column with the lowest average in a 2D array.
# Beginner Answer

arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
col_means = arr.mean(axis=0)
index = np.argmin(col_means)
print(index)
print(col_means[index])

