import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize


### Creating Data
'''
To create the dataset, a linear function with a known slope is created, and Gaussian noise is added to each point at random.  This allows comparison to the results and helps to see if the minimum solution is reasonable. 

$$y = 4.2x + \sigma$$   
'''

np.random.seed(42)
x = np.linspace(0, 1, 100)
y = 4.2*x + np.random.normal(size = 100)
plt.scatter(x, y)

## Problem 1

### Array of $\theta$'s
'''
**5 Points**

Below, create an array of possible $\theta$ values using `np.linspace`.  Create 100 values starting at 3 and ending at 5.  Assign your solution as an array to `thetas` below.
'''
thetas = np.linspace(3, 5, 100)

# Answer check
print(type(thetas))
print(thetas.shape)

## Problem 2

### Loss Function
'''
**5 Points**

Now, complete the function `l2_loss` below that accepts a single `theta` value as input and calculates the mean squared error based on the true y-values and the given theta.


The function should return a single float value representing the mean squared error.
'''

def l2_loss(theta):
    y_pred = theta * x
    mse = np.mean((y - y_pred) ** 2)
    return mse

## Problem 3

### Using `scipy` to minimize `l2_loss`
'''
**5 Points**

Use the `minimize` function that has been imported from `scipy.optimize` to find the minimum value of `l2_loss` using `x0 = 4`.  Assign your results to the `minimum_theta` variable below.  

Next, use the `minimum_theta.x` attribute to examine the solution and assign as a numpy array to `theta_solution` below.
'''

minimum_theta = minimize(l2_loss, x0=4)
theta_solution = minimum_theta.x

print(type(theta_solution))
print(theta_solution)

plt.plot(thetas, [l2_loss(i) for i in thetas])
plt.plot(theta_solution, l2_loss(theta_solution), 'ro', label = f'solution: {np.round(theta_solution[0], 3)}')
plt.legend();
plt.title(r'Minimizing Mean Squared Error given $\theta$');
plt.xlabel(r'$\theta$')
plt.ylabel('MSE')
plt.show()