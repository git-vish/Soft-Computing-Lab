import numpy as np
import keras

# STEP-1: initializing data
xt = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
yt = np.array([[0], [1], [1], [0]])

# STEP-2: creating nn model
model = keras.models.Sequential()
model.add(keras.layers.Dense(32, input_dim=2, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='rmsprop')

# STEP-3: learning
model.fit(xt, yt, epochs=1000)

# STEP-4: printing results
y_hat = model.predict(xt)
print('\nResults: ')
print('x1 \t x2 \t xor')
for x, y in zip(xt, y_hat):
    print(x[0], '\t', x[1], '\t', round(y[0], 3))
