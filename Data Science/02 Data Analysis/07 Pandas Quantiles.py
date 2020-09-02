# Quantiles are cut points dividing the range of the data into
# continuous intervals with an equal number of observations.
# Median is the only cut point in 2-quantiles,
# such that 50% of the data is below the median with the other half above it.
# Quartiles let us quickly divide a set of data into four groups,
# making it easy to see which of the four groups a particular data point is in.
# Quartiles are then 4-quantiles, that is, 25% of the data are between the
# minimum and first quartile, the next is 25% between the first quartile
# and median, the next 25% is between the median and the third quartile,
# and the last 25% of the data lies between the third quartile and the maximum.

import pandas as pd

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])

print(sales.quantile([0.33, 0.66, 0.75, 1]))
