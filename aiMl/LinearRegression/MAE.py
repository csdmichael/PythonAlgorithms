import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.optimize import minimize

np.random.seed(42)
x = np.linspace(0, 1, 100)
y = 4.2*x + np.random.normal(size = 100)
plt.scatter(x, y)

## Problem 1

### A MAE loss function
'''
**5 Points**

Complete the `mae` function below that takes in a value for $\theta$.

Your function should compute and return the mean absolute error based on the model $y = \theta*x$.  
'''
def mae_loss(theta):
    """
    This function accepts an array of thetas
    and returns the mean absolute error based
    on np.mean(|(theta*xi - yi)|)
    
    Arguments
    ---------
    theta: float
           Values to use for parameter
           of regression model.
            
    Returns
    -------
    mse: np.float
         Mean Absolute Error
    """
    y_pred = theta * x
    mae_value = np.mean(np.abs(y_pred - y))
    return mae_value

mae = mae_loss(8)
print(mae)
print(type(mae))

## Problem 2

### Minimizing the MAE Loss
'''
**5 Points**

Use the `minimize` function imported from `scipy.optimize` to determine the value for `mae_loss` that minimizes the Mean Absolute Error loss function starting at `x0 = 4`.  Assign this result to `minimum_theta `.

Next, use the `minimum_theta.x[0]` attribute to assign the solution as a float to `theta_mae` below.
'''
theta_mae = ''
# Your code here
minimum_theta = minimize(mae_loss, x0=4)
theta_mae = minimum_theta.x[0]

# Answer check
print(type(theta_mae))
print(theta_mae)

## Problem 3

### Uncovering the true $\theta$
'''
**5 Points**

Assuming that the true relationship between $x$ and $y$ was determined by a model with $\theta = 4.2$, which loss function better approximated the true value for $\theta$ here?  Enter your answer as a string -- either 'mse' or 'mae' -- below to the variable `better_loss`.
'''

def l2_loss(theta):
    y_pred = theta * x
    mse = np.mean((y - y_pred) ** 2)
    return mse


better_loss = ''
# Your code here
mae_loss = mae_loss(4.2)
mse_loss = l2_loss(4.2)
print(f"MAE Loss: {mae_loss}, MSE Loss: {mse_loss}")
better_loss = 'mae'
# Answer check
print(better_loss)
print(type(better_loss))