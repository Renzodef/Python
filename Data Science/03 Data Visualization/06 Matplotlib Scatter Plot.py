import pandas as pd
import os
import matplotlib.pyplot as plt

# Changing the current directory in the one of the .py file
os.chdir(os.path.dirname(__file__))
execution_path = os.getcwd()

presidents_df = pd.read_csv("president_heights_party.csv", index_col="name")

plt.scatter(presidents_df["height"], presidents_df["age"],
            marker="<", color="b")
plt.xlabel("height")
plt.ylabel("age")
plt.title("U.S. presidents")
plt.show()

# Plotting with Pandas directly
presidents_df.plot(kind="scatter", x="height", y="age",
                   title="U.S. presidents")
plt.show()
