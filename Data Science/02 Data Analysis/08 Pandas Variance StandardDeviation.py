import pandas as pd

# In probability and statistics,
# variance is the mean squared deviation of each data point
# from the mean of the entire dataset.

# You can think of it as how far apart a set of numbers are spread out
# from their average value.
# Standard deviation (std) is the square root of variance.
# A high std implies a large spread, and a low std indicates a small spread,
# or most points are close to the mean.

const = pd.Series([2, 2, 2])

print(const.var())  # 0.0
print(const.std())  # 0.0

dat = pd.Series([2, 3, 4])

print(dat.mean())  # 3.0
print(dat.var())  # 1.0
print(dat.std())  # 1.0
