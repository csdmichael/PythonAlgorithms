import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 5 * X + np.random.randn(100, 1)  # y = 4 + 5x + noise

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train different regression models
lin_reg = LinearRegression()
ridge_reg = Ridge(alpha=0.2)  # L2 regularization
lasso_reg = Lasso(alpha=0.2)  # L1 regularization

lin_reg.fit(X_train, y_train)
ridge_reg.fit(X_train, y_train)
lasso_reg.fit(X_train, y_train)

# Predictions for plotting
X_plot = np.linspace(0, 2, 100).reshape(-1, 1)
y_pred_lin = lin_reg.predict(X_plot)
y_pred_ridge = ridge_reg.predict(X_plot)
y_pred_lasso = lasso_reg.predict(X_plot)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_train, y_train, color='gray', alpha=0.5, label="Training Data")
plt.scatter(X_test, y_test, color='red', alpha=0.7, label="Test Data")
plt.plot(X_plot, y_pred_lin, "b-", label="Linear Regression")
plt.plot(X_plot, y_pred_ridge, "g--", label="Ridge Regression (L2)")
plt.plot(X_plot, y_pred_lasso, "r-.", label="Lasso Regression (L1)")

plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear vs Ridge (L2) vs Lasso (L1) Regression")
plt.show()