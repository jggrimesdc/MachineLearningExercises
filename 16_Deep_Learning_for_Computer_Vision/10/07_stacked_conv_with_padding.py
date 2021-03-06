# example a deep cnn with padding
from keras.layers import Conv2D
from keras.models import Sequential

# create model
model = Sequential()
model.add(Conv2D(1, (3, 3), padding='same', input_shape=(8, 8, 1)))
model.add(Conv2D(1, (3, 3), padding='same'))
model.add(Conv2D(1, (3, 3), padding='same'))
# summarize model
model.summary()
