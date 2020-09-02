import pandas as pd

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])

print(sales.min())
print("\n")
print(sales.max())
print("\n")
print(sales.mean())
print("\n")
print(sales.median())
