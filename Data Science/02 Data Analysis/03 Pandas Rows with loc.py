import pandas as pd

wine_dict = {"red_wine": [3, 6, 5], "white_wine": [5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])

# We can access a row by the name using .loc:
print(sales.loc["adam"])
print("\n")
# We can also slice by index.
# Say we are interested in gathering information between adam and bob.
print(sales.loc["adam":"bob"])
