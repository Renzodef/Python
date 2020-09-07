# Python's version used: 3.8.3 64 bit
# pip install scikit-learn
# pip install pandas
# pip install matplotlib

from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt

# The data is built in scikit-learn and we will use load_boston
# to load the object that contains all the information.
boston_dataset = load_boston()

boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)

# As the name suggests, boston_dataset.feature_names
# contain names for all features.
# We then add the target into the DataFrame:
boston["MEDV"] = boston_dataset.target

# To check the first 5 rows, use boston.head(),
# for the ease of display, we select columns CHAS, RM, AGE, RAD, and MEDV:
print(boston[['CHAS', 'RM', 'AGE', 'RAD', 'MEDV']].head())

print("\n//////////////////////////////////\n")

# There are 506 records, and 14 columns including 13 features and the target.
print(boston.shape)  # (506, 14)

print("\n//////////////////////////////////\n")

# To check the summary statistics of the dataset
# (round to the second decimal place for better display):
print(boston.describe().round(2))

# It’s a good practice to visualize and inspect
# the distribution column by column.
# Here we look at CHAS and RM to verify our conclusions from the last part.
boston.hist(column='CHAS')
plt.show()
