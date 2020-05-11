# Python's version used: 3.8.2 64 bit
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install seaborn
# pip install scikit-learn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import linear_model
import os

# Change the working directory in the one of the .py file
# So we can import the .csv file everytime
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Loading the .csv file
data = pd.read_csv("Datasets/student-mat.csv", sep=";")

# Choosing only the desired columns
# G1 - first period grade (numeric: from 0 to 20)
# G2 - second period grade (numeric: from 0 to 20)
# G3 - final grade (numeric: from 0 to 20, output target
# studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
# failures - number of past class failures (numeric: n if 1<=n<3, else 4)
# absences - number of school absences (numeric: from 0 to 93)
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Printing the first 5 rows of the imported dataset
print("\n")
print(data.head())
print("\n")

# Visualizing the target variable in a plot
sns.countplot(x='G3', data=data, palette='hls')
plt.show()

# Creating an array modeled on the dataframe
# and dropping the column "G3" in this array
# The 1 is to select columns, 0 would select axis
X = np.array(data.drop("G3", 1))

# Creating an array modeled on the column "G3" of the dataframe
# since this is the column we want to predict"
y = np.array(data["G3"])

# Creating training and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.1)

# Choosing the model Linear Regression
linear = linear_model.LinearRegression()

# Fitting the model to the training sets
linear.fit(x_train, y_train)

# Computing the accuracy of the model on the test sets
accuracy = linear.score(x_test, y_test)
print("Model's Accuracy:", accuracy)
print("\n")

# Priting the coefficients and the intercept of the Linear Regression's equation
print("Coefficient:", linear.coef_)
print("Intercept:", linear.intercept_)
print("\n")

# Printing the predicted values of "G3"
# and compare them with the real values of the test set
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print("Predicted G3:", predictions[x], "Real G3:", y_test[x])
print("\n")

# Creating a new tuple
new_array = np.array([[15, 18, 2, 0, 6]])
print("New Tuple:", new_array)

# Predicting "G3" in the new tuple
new_prediction = linear.predict(new_array)
for x in range(len(new_prediction)):
    print("New Tuple's Value Prediction:", new_prediction[x])
print("\n")
