import pandas as pd

# In data science, data is usually more than one-dimensional,
# and of different data types; thus Series is not sufficient.
# DataFrames are 2darrays with both row and column labels.
# One way to create a DataFrame from scratch is to pass in a dict.

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
# Print the dataframe
print(sales)
print("\n")
# Print the selected column
print(sales["white_wine"])
print("\n")
# Print the dimensions of the dataframe
print(sales.shape)
print("\n")
# Print the number of elements of the dataframe
print(sales.size)
print("\n")
# Print the first row of the dataframe
print(sales.head(n=1))
print("\n")
# Print the last row of the dataframe
print(sales.tail(n=1))
print("\n")
# Print info about the dataframe
print(sales.info())
