import pandas as pd
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


auto = pd.read_csv('aiMl/Overfitting/data/auto.csv')
print(auto.head())

### The Sample
'''
Below, a sample of ten vehicles from the data is extracted.  These data will form our **training** data.  The data is subsequently split into `X_train` and `y_train`.  You are to use this smaller dataset to build your models on and explore their performance using the entire dataset.
'''
X = auto.loc[:,['horsepower']]
y = auto['mpg']
sample = auto.sample(10, random_state = 22)
X_train = sample.loc[:, ['horsepower']]
y_train = sample['mpg']
print(X_train)
print(y_train)
print(X.shape)

### Problem 1
#### Build the Model
'''
Using the training data from above, build a neural network model with the following specifications:
- The model should be a Sequential model.
- The model should have one hidden layer with 5 neurons and a ReLU activation function.
- The output layer should have one neuron (for regression) and no activation function.
- Compile the model using the Adam optimizer and mean squared error as the loss function.
'''
model = Sequential()
model.add(Dense(5, activation='relu', input_shape=(1,)))
model.add(Dense(1))
model.compile(optimizer=Adam(), loss='mean_squared_error')
print(model.summary())

### Problem 2
#### Train the Model
'''
Train the model using the training data for 100 epochs with a batch size of 2.
history = model.fit(X_train, y_train, epochs=100, batch_size=2, verbose=0)
'''
history = model.fit(X_train, y_train, epochs=100, batch_size=2, verbose=0)
print("Training complete.")

### Problem 3
#### Evaluate the Model
'''
Evaluate the model's performance on the entire dataset and print the mean squared error.
'''
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error on entire dataset: {mse}')

### Problem 4
#### Visualize Predictions using matplotlib
'''
Create a scatter plot of the actual vs predicted values using Plotly Express.
'''
import matplotlib.pyplot as plt
plt.scatter(y, predictions)
plt.xlabel('Actual MPG')
plt.ylabel('Predicted MPG')
plt.title('Actual vs Predicted MPG')
plt.show()



