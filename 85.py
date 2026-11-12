# 85. Normalize an array so its values range from 0 to 1.
# Beginner Answer

arr = np.array([10, 20, 30, 40])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)

