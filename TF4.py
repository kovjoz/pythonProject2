#Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

#Load dataset
url = "https://raw.githubusercontent.com/callxpert/datasets/master/iris.data.txt"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pd.read_csv(url, names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby("class").size())

#dataset.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()

dataset.hist()
dataset.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()

from pandas.plotting import scatter_matrix
scatter_matrix(dataset)
#plt.show()

array = dataset.values
X = array[:,0:4]
Y = array[:,4]
x_train, x_test, y_train, y_test = model_selection.train_test_split(X,Y,test_size=0.2,random_state=7)

model = KNeighborsClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(accuracy_score(y_test, predictions))



