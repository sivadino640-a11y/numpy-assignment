# 58. Extract a 2×2 sub-matrix from a 4×4 matrix.
# Beginner Answer

arr = np.arange(1, 17).reshape(4, 4)
sub = arr[1:3, 1:3]
print(sub)

