import tensorflow as tf
import numpy as np

print("TensorFlow version:", tf.__version__)

# data = load data
model = tf.keras.models.Sequential([])

model.compile(optimizer='sgd', loss='mse', metrics=['acc', 'f1_score'])
model.summary()
