# 86. Find the second-largest unique value in a NumPy array.
# Beginner Answer

arr = np.array([10, 50, 30, 50, 20])
unique = np.unique(arr)
second_largest = unique[-2]
print(second_largest)

