import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing


# load dataset
dataset = pd.read_csv("C:\\Users\\jkovacs\\Desktop\\Kaggle_Learn_Housing\\train.csv")


# split into input (X) and output (Y) variables
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# define features and labels
train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('SalePrice')
test_labels = test_features.pop('SalePrice')

#print(train_features.columns)
# data analysis by plotting

def plot(feature, x=None, y=None):
	plt.figure(figsize=(10, 8))
	plt.scatter(train_features[feature], train_labels, label='Data')
	if x is not None and y is not None:
		plt.plot(x, y, color='k', label='Predictions')
	plt.xlabel(feature)
	plt.ylabel('SalePrice')
	plt.legend()


"""features = ['1stFlrSF', 
             'TotRmsAbvGrd',
            'PoolArea', 'Fence', 'MSZoning', 'Neighborhood']"""


plot('ExterQual')
plt.show()

"""
# normalize
normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(train_features))

# model
model = keras.models.Sequential([
	normalizer,
	layers.Dense(units=12, activation='relu'),
	layers.Dense(units=64, activation='relu'),
	layers.Dense(units=64, activation='relu'),
	layers.Dense(units=1)
])

# loss and optimizer
#loss = keras.losses.MeanAbsoluteError()
loss = keras.losses.MeanSquaredLogarithmicError()
optim = keras.optimizers.Adam(learning_rate=0.02)

model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss=loss)

model.fit(
	train_features, train_labels,
	epochs=100,
	verbose=1,
	validation_split=0.2)

print("Test evaluate:")
model.evaluate(test_features, test_labels, verbose=1)

feature = 'GrLivArea'
range_min = np.min(train_features[feature]) - 10
range_max = np.max(train_features[feature]) + 10

x = tf.linspace(range_min, range_max, 200)
y = model.predict(x)
plot(feature, x, y)
plt.show()

"""