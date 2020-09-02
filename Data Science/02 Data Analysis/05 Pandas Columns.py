import pandas as pd

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])

# We can retrieve an entire column by name.
# First we access all the column names:
print(sales.columns)
print("\n")
print(sales['white_wine'])
print("\n")
print(sales[['red_wine', 'white_wine']])
