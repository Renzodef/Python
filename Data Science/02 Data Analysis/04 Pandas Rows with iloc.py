import pandas as pd

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])

# If we do know the integer position(s), we can use .iloc to access the row(s).
print(sales.iloc[0])
print("\n")
print(sales.iloc[0:2])
