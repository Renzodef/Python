# The Series is one building block in pandas.
# Pandas Series is a one-dimensional labeled array that can hold data
# of any type (integer, string, float, python objects, etc.),
# similar to a column in an excel spreadsheet.
# The axis labels are collectively called index.

import numpy as np
import pandas as pd

print(pd.Series(np.array([1, 2, 3]), index=["a", "b", "c"]))  # from a 1darray
