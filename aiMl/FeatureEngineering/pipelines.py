import numpy as np
import pandas as pd
import warnings
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
warnings.filterwarnings("ignore")

### The Data
'''
The data will again be the automobile dataset.  You are to use the pipelines to build quadratic features and linear models using `horsepower` to predict `mpg`.   
'''

auto = pd.read_csv('aiMl/FeatureEngineering/data/auto.csv')
print(auto.head())

## Problem 1

### Creating a `Pipeline`
'''
**4 Points**

Use `Pipeline` to create a pipeline object. Inside the pipeline object, define a tuple where the first element is a string identifier `quad_features` and the second element is an instance of `PolynomialFeatures` of degree `2`. Inside the pipeline define another tuple where the first element is a string identifier `quad_model`, and the second element is an instance of `LinearRegression`. Assign the pipeline object to the variable `pipe`.
'''
pipe = Pipeline([
    ('quad_features', PolynomialFeatures(degree=2)),
    ('quad_model', LinearRegression())
])

## Problem 2

### Fitting the Pipeline
'''
**4 Points**

Complete the code below according to the following instructions:

- Assign to the variable `X` the values of the `horsepower` of `auto`.
- Assign to the variable `y` the values of the `mpg` of `auto`.
- Use the function `fit` on `pipe` to train your model on `X` and `y`.
- Determine the `mean_squared_error` of your model, and assign the value as a float to `quad_pipe_mse` below.  
'''

X = auto[['horsepower']].values
y = auto['mpg'].values
pipe.fit(X, y)
y_pred = pipe.predict(X)
quad_pipe_mse = float(mean_squared_error(y, y_pred))
print(f"Mean Squared Error of the pipeline model: {quad_pipe_mse}")

## Problem 3

### Examining the Coefficients
'''
**4 Points**

Now, to examine the coefficients, use the `.named_steps` attribute on the `pipe` object to extract the regressor.  Assign the model to `quad_reg` below.  

Extract the coefficients from the model and assign these as an array to the variable `coefs`.
'''
quad_reg = pipe.named_steps['quad_model']
coefs = quad_reg.coef_
print(f"Coefficients of the quadratic model: {coefs}")

## Problem 4

### Considering the Bias 
'''
**4 Points**

Not that your coefficients have 3 values.  Your model also contains an intercept term though, and this leads to one more value than expected from a quadratic model with one input feature.  This is due to the inclusion of the bias term using `PolynomialFeatures` and the intercept term added with the `fit_intercept = True` default setting in the regressor.  


To get the appropriate model coefficients and intercept, you can set `include_bias = False` in the `PolynomialFeatures` transformer.  

Complete the code according to the instructions below:

- Use `Pipeline` to create a pipeline object. Inside the pipeline object, define a a tuple where the first element is a string identifier `quad_features` and the second element is an instance of `PolynomialFeatures` of degree `2` with `include_bias = False`. Inside the pipeline, define another tuple where the first element is a string identifier `quad_model`, and the second element is an instance of `LinearRegression`. Assign the pipeline object to the variable `pipe_no_bias`.
- Use the `fit` function on `pipe_no_bias` to train your model on `X` and `y`. 
- Use the `mean_squared_error` function to calculate the MSE between `y` and `pipe_no_bias.predict(X)`. Assign the result as a float `no_bias_mse`.
'''

pipe_no_bias = Pipeline([
    ('quad_features', PolynomialFeatures(degree=2, include_bias=False)),
    ('quad_model', LinearRegression())
])

pipe_no_bias.fit(X, y)
y_no_bias_pred = pipe_no_bias.predict(X)
no_bias_mse = float(mean_squared_error(y, y_no_bias_pred))
print(f"Mean Squared Error of the pipeline model without bias: {no_bias_mse}")

## Problem 5

### Building a Cubic Model with `Pipeline`
'''
**4 Points**

Complete the code according to the instructions below:

- Use `Pipeline` to create a pipeline object. Inside the pipeline object, define a a tuple where the first element is a string identifier `quad_features` and the second element is an instance of `PolynomialFeatures` of degree `3` with `include_bias = False`. Inside the pipeline define another tuple where the first element is a string identifier `quad_model`, and the second element is an instance of `LinearRegression`. Assign the pipeline object to the variable `cubic_pipe`.
- Use the `fit` function on `cubic_pipe` to train your model on `X` and `y`. 
- Use the `mean_squared_error` function to calculate the MSE between `y` and `cubic_pipe.predict(X)`. Assign the result as a float to `no_bias_mse`.
'''

cubic_pipe = Pipeline([
    ('quad_features', PolynomialFeatures(degree=3, include_bias=False)),
    ('quad_model', LinearRegression())
])

cubic_pipe.fit(X, y)
y_cubic_pred = cubic_pipe.predict(X)
cubic_mse = float(mean_squared_error(y, y_cubic_pred))
print(f"Mean Squared Error of the cubic pipeline model: {cubic_mse}")

## Problem 6

### Making Predictions on New Data
'''
**4 Points**

Finally, one of the main benefits derived from using a Pipeline is that you do not need to engineer new polynomial features when predicting with new data.  Use your cubic pipeline to predict the `mpg` for a vehicle with 200 horsepower.  Assign your prediction as a numpy array to `cube_predict` below.
'''

new_data = np.array([[200]])
cube_predict = cubic_pipe.predict(new_data)
print(f"Predicted mpg for a vehicle with 200 horsepower: {cube_predict}")
import numpy as np
print(f"Predicted mpg for a vehicle with 200 horsepower: {cube_predict}")
