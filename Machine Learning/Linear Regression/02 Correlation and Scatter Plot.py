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

# To understand the relationship among features (columns),
# a correlation matrix is very useful in the exploratory data analysis.
# Correlation measures linear relationships between variables.
# We can construct a correlation matrix to show correlation coefficients
# between variables.
# It is symmetric where each element is a correlation coefficient
# ranging from -1 and 1.
# A value near 1 (resp. -1) indicates a strong positive (resp. negative)
#  correlation between variables.
# We can create a correlation matrix using the "corr" function:
corr_matrix = boston.corr().round(2)
print(corr_matrix)

# We noticed that RM and MEDV are positively correlated.
# Recall that scatter plot is a useful tool to display the relationship
# between two features; let’s take a look at the scatter plot:
boston.plot(kind="scatter", x="RM", y="MEDV", figsize=(8, 6))
plt.show()
