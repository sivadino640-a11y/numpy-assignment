# 75. Split a 2D matrix into two vertical sections.
# Beginner Answer

arr = np.arange(1, 13).reshape(3, 4)
parts = np.vsplit(arr, 2)  # requires an even number of rows
print(parts)

