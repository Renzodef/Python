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

"""
# Loading the .csv file
Attribute Information:
To construct the data, seven geometric parameters of wheat kernels were measured:
1. area A,
2. perimeter P,
3. compactness C = 4*pi*A/P^2,
4. length of kernel,
5. width of kernel,
6. asymmetry coefficient
7. length of kernel groove.
All of these parameters were real-valued continuous.
8. The examined group comprised kernels belonging to three different varieties of wheat:
   Kama, Rosa and Canadian (respectively 1, 2 and 3 in the dataset).
"""
data = pd.read_csv("Datasets/seeds_dataset.csv",
                   header=None,
                   delim_whitespace=True)
data.columns = [
    'Area', 'Perimeter', 'Compactness', 'Lenght of kernel', 'Width of kernel',
    'Asymmetry coefficient', 'Lenght of kernel groove', 'Variety of wheat'
]

# Printing the first 5 rows of the imported dataset
print("\n")
print(data.head())
print("\n")

# Visualizing the target variable in a plot
sns.countplot(x="Variety of wheat", data=data, palette='hls')
plt.show()

# Creating an array modeled on the dataframe
# and dropping the last column in this array
# The 1 is to select columns, 0 would select axis
X = np.array(data.drop("Variety of wheat", 1))

# Creating an array modeled on the last column of the dataframe
# since this is the column we want to predict"
y = np.array(data["Variety of wheat"])

# Creating training and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2)

# Choosing the model Linear Regression
# Increasing the default max_iter in order to reach convergence
logreg = linear_model.LogisticRegression(max_iter=5000)

# Fitting the model to the training sets
logreg.fit(x_train, y_train)

# Predictions on the test set
y_pred = logreg.predict(x_test)

# Calculating and plotting the confusion matrixs
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
# Need to change in range(3) because the matrix will be 3x3
df_cm = pd.DataFrame(cnf_matrix, range(3), range(3))
plt.figure(figsize=(5.5, 5.5))
sns.set(font_scale=1.2)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="viridis", fmt='g')
plt.title('Confusion matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

# Printing the evaluation metrics
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
# Need to add the average's flag for Multinomial Logistic Regression
print("Precision:", metrics.precision_score(y_test, y_pred, average='micro'))
print("Recall:", metrics.recall_score(y_test, y_pred, average='micro'))
print("\n")

# Creating a new tuple
new_array = np.array([[19.55, 15.76, 0.21, 4.362, 3.10, 2.9, 5.21]])
print("New Tuple:", new_array)

# Predicting "Variety of wheat" in the new tuple
new_prediction = logreg.predict(new_array)
for x in range(len(new_prediction)):
    print("New Tuple's Value Prediction:", new_prediction[x])
print("\n")