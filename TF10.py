import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np
import itertools


from sklearn.model_selection import train_test_split
import math

tf.random.set_seed(42)

train_data = pd.read_csv("C:\\Users\\jkovacs\\Desktop\\Kaggle_Learn_Housing\\train.csv")
test_data = pd.read_csv("C:\\Users\\jkovacs\\Desktop\\Kaggle_Learn_Housing\\test.csv")

#features = ['1stFlrSF', '2ndFlrSF', 'Neighborhood', 'YearBuilt', 'GarageCars',
 #           'Condition1', 'Condition2', 'BedroomAbvGr', 'FullBath', 'LandContour', 'BldgType', 'HouseStyle',
  #          'OverallQual', 'OverallCond', 'ExterCond', 'Foundation', 'GarageQual', 'GarageCond']


features = ['1stFlrSF', '2ndFlrSF', 'Neighborhood', 'YearBuilt',
            'Condition1', 'BedroomAbvGr', 'FullBath', 'LandContour', 'BldgType',
            'OverallQual', 'OverallCond', 'ExterCond', 'Foundation', 'GarageCond', 'GarageType', 'GarageArea']

#print(' Train - Neighborhood: ', train_data['Neighborhood'].value_counts())
#print(' Test - Neighborhood: ', test_data['Neighborhood'].value_counts())


def feature_check(column):
    print(column)
    print("train:")
    train_list = list(set(train_data[column]))
    print(train_list)
    print(len(train_list))

    print("test:")
    test_list = list(set(test_data[column]))
    print(test_list)
    print(len(test_list))
    print("-"*30)


#for item in features:
 #   feature_check(item)


X2 = train_data[features].copy()
X2_one_hot = pd.get_dummies(X2)
print("Train shape:", X2_one_hot.shape)

X_test = test_data[features].copy()
X_test_onehot = pd.get_dummies(X_test)
# np conversion
#X_test = np.asarray(X_test).astype(np.float)
print("Test shape:", X_test_onehot.shape)

y1 = train_data.pop("SalePrice")


# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X2_one_hot, y1, train_size=0.8, random_state=3)

input_neur = X2_one_hot.shape[1]

# create model
model2 = tf.keras.Sequential([
    tf.keras.layers.Dense(input_neur, activation="relu"),
    tf.keras.layers.Dense(200, activation="relu"),
    tf.keras.layers.Dense(200, activation="relu"),
    tf.keras.layers.Dense(200, activation="relu"),
    tf.keras.layers.Dense(1, activation="linear")
])


# compile model
model2.compile(loss="mae", optimizer=tf.keras.optimizers.Adam(learning_rate=0.0022), metrics="mae")
#model2.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.0022), metrics="mse")

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=50)

# fit model
history = model2.fit(X_train, y_train, epochs=300, callbacks=callback, verbose=False)

# predictions
preds = model2.predict(X_valid)  # numpy.ndarray

# eval
print('Validation MAE:', mean_absolute_error(y_valid, preds))
#print('Validation MSE:', mean_squared_error(y_valid, preds), '-->', math.sqrt(mean_squared_error(y_valid, preds)))

# visualize
list_X_valid = X_valid['1stFlrSF'].copy()

plt.figure(figsize=(10, 7))
plt.scatter(list_X_valid, preds, c="b", label="Pred data")
plt.scatter(list_X_valid, y_valid, c="r", label="Real data")
plt.legend()
plt.show()

# plot training curve, using history.history
pd.DataFrame(history.history).plot()
plt.xlabel = "epochs"
plt.show()

# Test data predictions
preds_test = model2.predict(X_test_onehot)

preds_out = np.ndarray.tolist(preds_test)
preds_out2 = []
for item in preds_out:
    for x in item:
        preds_out2.append(x)


#print(test_data['Id'])

# output file
output = pd.DataFrame({'Id': test_data['Id'],
                       'SalePrice': preds_out2})
output.to_csv('C:\\Users\\jkovacs\\Desktop\\submission.csv', index=False)
