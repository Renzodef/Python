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
from sklearn import metrics
import os

# Change the working directory in the one of the .py file
# So we can import the .csv file everytime
try:
    os.chdir(os.path.dirname(__file__))
except:
    pass

# Loading the .csv file
# Attribute informations:
# 1. Age of patient at time of operation (numerical)
# 2. Patient's year of operation (year - 1900, numerical)
# 3. Number of positive axillary nodes detected (numerical)
# 4. Survival status (class attribute) =>
#    1 = the patient survived 5 years or longer
#    2 = the patient died within 5 year
data = pd.read_csv("Datasets/haberman.csv", sep=",", header=None)
data.columns = [
    'Operation age', 'Operation year', 'Axillary nodes', 'Survival status'
]

# Printing the first 5 rows of the imported dataset
print("\n")
print(data.head())
print("\n")

# Visualizing the target variable in a plot
sns.countplot(x='Survival status', data=data, palette='hls')
plt.show()

# Creating an array modeled on the dataframe
# and dropping the last column in this array
# The 1 is to select columns, 0 would select axis
X = np.array(data.drop("Survival status", 1))

# Creating an array modeled on the last column of the dataframe
# since this is the column we want to predict"
y = np.array(data["Survival status"])

# Creating training and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2)

# Choosing the model Linear Regression
# Increasing the default max_iter in order to reach convergence
logreg = linear_model.LogisticRegression()

# Fitting the model to the training sets
logreg.fit(x_train, y_train)

# Predictions on the test set
y_pred = logreg.predict(x_test)

# Calculating and plotting the confusion matrixs
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cnf_matrix, range(2), range(2))
plt.figure(figsize=(5.5, 5.5))
sns.set(font_scale=1.2)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="viridis", fmt='g')
plt.title('Confusion matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

# Printing the evaluation metrics
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))
print("\n")

# Creating a new tuple
new_array = np.array([[63, 61, 2]])
print("New Tuple:", new_array)

# Predicting "Survival status" in the new tuple
new_prediction = logreg.predict(new_array)
for x in range(len(new_prediction)):
    print("New Tuple's Value Prediction:", new_prediction[x])
print("\n")
