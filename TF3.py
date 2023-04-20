import tensorflow as tf
import numpy as np

# define a tensor
tens2 = tf.Variable([["elso", "masodik"], ["alfa", "beta"], ["first", "second"]], tf.string)

print(tf.rank(tens2))
print(tf.shape(tens2))

# reshape a tensor
tens2_rs = tf.reshape(tens2, [2,3,1])
#print(tens2_rs)

rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(rank_1_tensor.numpy())
print("First:", rank_1_tensor[0].numpy())
print("Second:", rank_1_tensor[1].numpy())
print("Last:", rank_1_tensor[-1].numpy())
print("Reversed:", rank_1_tensor[::-1].numpy())