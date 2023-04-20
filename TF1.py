"""
First ML model: F = C * 1.8 + 32
"""

import tensorflow as tf
import numpy as np
import logging
import matplotlib.pyplot as plt

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# Set up training data
c = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)    # Input called Feature
f = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)  # Output called Labels

# Check data
# for l, m in enumerate(c):
#     print("{} Celsius = {} Fahrenheit".format(m, f[l]))

# Single layer with single neuron, input: a number
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

#model = tf.keras.Sequential([tf.keras.layers.Dense(units=4, input_shape=[1])])  # try more layers and neurons
#model.add(tf.keras.Sequential([tf.keras.layers.Dense(units=4)]))    # try more layers and neurons
#model.add(tf.keras.Sequential([tf.keras.layers.Dense(units=1)]))  # try more layers and neurons

# Compile the model: define loss and optimizer
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.11))

# Train the model
history = model.fit(c, f, epochs=900, verbose=False)

# Prediction
print("10 (50): ", model.predict([10.0]))
print("20 (68): ", model.predict([20.0]))


# Display statistics
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(history.history['loss'])
plt.show()


