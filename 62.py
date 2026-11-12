# 62. Use boolean indexing to find values between 20 and 80.
# Beginner Answer

arr = np.array([10, 20, 35, 60, 80, 90])
result = arr[(arr >= 20) & (arr <= 80)]
print(result)

