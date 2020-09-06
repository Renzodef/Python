import pandas as pd
import os
import matplotlib.pyplot as plt

# Changing the current directory in the one of the .py file
os.chdir(os.path.dirname(__file__))
execution_path = os.getcwd()

presidents_df = pd.read_csv("president_heights_party.csv", index_col="name")

party_cnt = presidents_df["party"].value_counts()

plt.style.use("ggplot")
party_cnt.plot(kind="bar")
plt.show()
