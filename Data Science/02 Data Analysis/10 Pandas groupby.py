import pandas as pd
import os

# Changing the current directory in the one of the .py file
os.chdir(os.path.dirname(__file__))
execution_path = os.getcwd()

presidents_df = pd.read_csv("president_heights_party.csv", index_col="name")

# To find the value based on a condition, we can use the groupby operation.
print(presidents_df.groupby("party").mean())
