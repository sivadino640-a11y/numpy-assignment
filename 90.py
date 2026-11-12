# 90. Find the frequency of every unique value.
# Beginner Answer

arr = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(arr, return_counts=True)
for value, count in zip(values, counts):
    print(value, count)

