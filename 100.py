import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 70, 60],
    [92, 88, 95],
    [45, 55, 50],
    [30, 40, 35]
])

names = np.array(['A', 'B', 'C', 'D', 'E'])

total = marks.sum(axis=1)
average = marks.mean(axis=1)

highest_index = np.argmax(total)
lowest_index = np.argmin(total)

print('Total:', total)
print('Average:', average)
print('Highest scorer:', names[highest_index], total[highest_index])
print('Lowest scorer:', names[lowest_index], total[lowest_index])

subject_average = marks.mean(axis=0)
print('Subject-wise average:', subject_average)

passed = np.all(marks >= 40, axis=1)
print('Pass count:', np.sum(passed))
print('Fail count:', np.sum(~passed))

for name, avg in zip(names, average):
    if avg >= 90:
        grade = 'A+'
    elif avg >= 80:
        grade = 'A'
    elif avg >= 70:
        grade = 'B'
    elif avg >= 60:
        grade = 'C'
    elif avg >= 40:
        grade = 'D'
    else:
        grade = 'F'
    print(name, grade)

rank_order = np.argsort(total)[::-1]
ranks = np.empty_like(rank_order)
ranks[rank_order] = np.arange(1, len(total) + 1)
print('Ranks:', ranks)

class_average = average.mean()
print('Class average:', class_average)
print('Above class average:', names[average > class_average])

