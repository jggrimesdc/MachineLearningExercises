# Example of one output for whole sequence
from keras.layers import LSTM
from keras.models import Sequential
from numpy import array

# define model where LSTM is also output layer
model = Sequential()
model.add(LSTM(1, input_shape=(3, 1)))
model.compile(optimizer='adam', loss='mse')
# input time steps
data = array([0.1, 0.2, 0.3]).reshape((1, 3, 1))
# make and show prediction
print(model.predict(data))
