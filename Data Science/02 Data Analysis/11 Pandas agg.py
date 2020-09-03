import pandas as pd
import numpy as np
import os

# Changing the current directory in the one of the .py file
os.chdir(os.path.dirname(__file__))
execution_path = os.getcwd()

presidents_df = pd.read_csv('president_heights_party.csv', index_col='name')


# We can also perform multiple operations on the
# # groupby object using .agg() method.
print(presidents_df.groupby('party')['height'].agg(['min', np.median, max]))
