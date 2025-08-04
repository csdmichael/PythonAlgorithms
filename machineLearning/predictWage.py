import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Sample data: [Age, Experience], Wage
X = np.array([
    [25, 1],
    [30, 5],
    [35, 7],
    [40, 10],
    [45, 15],
    [50, 20],
    [55, 25],
    [60, 30]
], dtype=np.float32)

y = np.array([30, 50, 60, 80, 100, 120, 140, 160], dtype=np.float32)

# Normalize inputs for better training
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_scaled = (X - X_mean) / X_std

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(2,))
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_scaled, y, epochs=500, verbose=0)

# Make predictions
predicted_wage = model.predict(X_scaled)

# Plot results
plt.scatter(X[:, 0], y, color='blue', label='Actual Wage')
plt.scatter(X[:, 0], predicted_wage, color='red', label='Predicted Wage')
plt.xlabel('Age')
plt.ylabel('Wage')
plt.legend()
plt.title('Linear Regression: Wage vs Age (and Experience)')
plt.show()
