# 76. Split a 2D matrix into two horizontal sections.
# Beginner Answer

arr = np.arange(1, 13).reshape(3, 4)
parts = np.hsplit(arr, 2)
print(parts)

