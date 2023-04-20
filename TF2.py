import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


mnist = tf.keras.datasets.mnist #28*28 images of hand written digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)


# MODEL1
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  #Input layer
model.add(tf.keras.layers.Dense(200, activation=tf.nn.relu))  #Hidden1 layer 128 neurons
model.add(tf.keras.layers.Dense(200, activation=tf.nn.relu))  #Hidden2 layer 128 neurons
model.add(tf.keras.layers.Dense(200, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.4))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  #Output layer, 10=digits, probability distribution

# COMPILE
model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])   #'adam' lehet más is, ez egy elterjedt

# FIT
model.fit(x_train, y_train, epochs=10)

val_loss, val_acc = model.evaluate(x_test, y_test)
#print("vld_loss: ", val_loss, "vld_acc: ", val_acc)


prd = model.predict([x_test])
print(np.argmax(prd[7]))

plt.imshow(x_test[7])
plt.show()


# MODEL2
"""
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.4),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=6)

# TEST
print("Test: ")
model.evaluate(x_test,  y_test, verbose=2)
"""
