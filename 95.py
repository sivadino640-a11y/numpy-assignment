# 95. Find the percentage of missing values represented by NaN.
# Beginner Answer

arr = np.array([10, np.nan, 20, np.nan, 30])
missing_percent = np.isnan(arr).sum() / arr.size * 100
print(missing_percent)

