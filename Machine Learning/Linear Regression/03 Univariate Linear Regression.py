# Python's version used: 3.8.3 64 bit
# pip install scikit-learn
# pip install pandas

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_boston

boston_dataset = load_boston()
boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)
boston["MEDV"] = boston_dataset.target

X = boston[["RM"]]
Y = boston["MEDV"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,
                                                    random_state=1)

model = LinearRegression()
model.fit(X_train, Y_train)
intercept = model.intercept_
# Array of coefficients, but in this file only has size 1
# since X is just one attribute
RM_coefficient = model.coef_
print("\nModel:\nMEDV = " + str(intercept) + " + "
      + str(RM_coefficient[0]) + " * RM")

# New RM to predict new MEDV
new_RM = 6.5
new_MEDV = intercept + RM_coefficient[0] * new_RM
print("\nPrediction for RM = " + str(new_RM) + ":"
      "\nMEDV = " + str(intercept) + " + " + str(RM_coefficient[0]) +
      " * " + str(new_RM) + " = " + str(new_MEDV))
