import pandas as pd
import os
import matplotlib.pyplot as plt

# Changing the current directory in the one of the .py file
os.chdir(os.path.dirname(__file__))
execution_path = os.getcwd()

presidents_df = pd.read_csv("president_heights_party.csv", index_col="name")

plt.hist(presidents_df["height"], bins=5)
plt.show()

# Plotting with Pandas directly
presidents_df["height"].plot(kind="hist", title="height", bins=5)
plt.show()
