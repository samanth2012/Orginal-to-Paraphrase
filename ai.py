import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

import keras
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Masking
from keras import Sequential

from keras.datasets import imdb

import warnings

n = 5000
embedi = 32 
o_l = 100

model = Sequential() 
model.add(Embedding(n, embedi, input_length=500)) 
model.add(LSTM(o_l)) 
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy']) 
model.summary()

model.save('moviereviews3.h5')
