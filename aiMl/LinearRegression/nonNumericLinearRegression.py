import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

### The Dataset
'''
The `diamonds` dataset from Seaborn is loaded and displayed below.  You will explore models that use both the `cut` and `color` features independently and models using all possible features.  To begin, you will use pandas `get_dummies` function to produce the dummy encoded data.  Your dummy encoded data should have as many features as there are unique values in the data.
'''

import urllib

diamonds = None

try:
    diamonds = sns.load_dataset('diamonds')
except:
    diamonds_dataset_uri = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"
    with urllib.request.urlopen(diamonds_dataset_uri) as response:
        diamonds = pd.read_csv(response) 

print(diamonds.head())


## Problem 1

### Unique Values in `cut` and `color`
'''
**4 Points**

Using the `cut` and `color` columns, determine the number of unique values in each column.  Assign the number of unique values in each feature as integers to `num_cuts` and `num_color` below.  
'''

num_cuts = diamonds['cut'].nunique()
num_color = diamonds['color'].nunique()

# Answer check
print(f'Number of unique values in cut: {num_cuts}')
print(f'Number of unique values in color: {num_color}')

## Problem 2

### Encoding the `cut` column
'''
**4 Points**

Use the `get_dummies()` function to create a dummy encoded version of the `cut` column.  Assign your encoded data as a DataFrame to the variable `cut_encoded` below.  
'''

cut_encoded = pd.get_dummies(diamonds['cut'], prefix='cut')

# Answer check
print(cut_encoded.head())

## Problem 3

### A Regression model on `cut`
'''
**4 Points**

Use the `get_dummies()` function to create a dummy encoded version of the `cut` column and assign the result to the variable `X`.

To the variable `y`, assign the column `price` in the `diamonds` dataset.

Use the `LinearRegression` estimator  with argument `fit_intercept = False` to build a regression model. Next, use the `fit()` function with arguments `X` and `y`  to predict the `price` column.  

Assign the model to `cut_linreg` below.  
'''
X = pd.get_dummies(diamonds['cut'], prefix='cut')
y = diamonds['price']
cut_linreg = LinearRegression(fit_intercept=False)
cut_linreg.fit(X, y)

# Answer check
print(cut_linreg)
print(type(cut_linreg))
print(cut_linreg.coef_)

## Problem 4

### Interpreting the results
'''
**4 Points**

Compare the coefficients of the model.  Which cut does your model predict as the price for a diamond with an `ideal_cut`?  Assign your solution as a float rounded to two decimal places to `ideal_cut_prediction` below.  
'''

ideal_cut_index = X.columns.get_loc('cut_Ideal')
ideal_cut_prediction = round(cut_linreg.coef_[ideal_cut_index], 2)

# Answer check
print(f'Predicted price for ideal cut: {ideal_cut_prediction}')

## Problem 5

### Building a model on `clarity`
'''
**4 Points**

Use the `get_dummies()` function to create a dummy encoded version of the `clarity` column and assign the result to the variable `X`.

To the variable `y`, assign the column `price` in the `diamonds` dataset.

Use the `LinearRegression` estimator  with argument `fit_intercept = False` to build a regression model. Next, use the `fit()` function with arguments `X` and `y`  to predict the `price` column.  

Assign the model to `clarity_linreg` below.  
'''

X = pd.get_dummies(diamonds['clarity'], prefix='clarity')
y = diamonds['price']
clarity_linreg = LinearRegression(fit_intercept=False)
clarity_linreg.fit(X, y)
# Answer check
print(clarity_linreg)
print(type(clarity_linreg))
print(clarity_linreg.coef_)

## Problem 6

### Interpreting the results
'''
**4 Points**

Examine your coefficients and compare these to the columns of the dummy encoded version of the `clarity` column.  What price does your model predict for a diamond with clarity `SI2`?  Assign your results as a float rounded to 2 decimal places to `clarity_si2_prediction`.
'''

si2_index = X.columns.get_loc('clarity_SI2')
clarity_si2_prediction = round(clarity_linreg.coef_[si2_index], 2)

# Answer check
print(f'Predicted price for clarity SI2: {clarity_si2_prediction}')

## Problem 7

### A Model with `cut`, `clarity`, and `carat`
'''
**4 Points**

Use the `get_dummies()` function to create a dummy encoded version of the `carat`, `cut`, and `clarity` columns and assign the result to the variable `X`.

To the variable `y`, assign the column `price` in the `diamonds` dataset.

Use the `LinearRegression` estimator  with argument `fit_intercept = False` to build a regression model. Next, use the `fit()` function with arguments `X` and `y`  to predict the `price` column.  

Assign the model to `ccc_linreg` below. 
'''
X = pd.get_dummies(diamonds[['carat', 'cut', 'clarity']], drop_first=True)
y = diamonds['price']
ccc_linreg = LinearRegression(fit_intercept=False)
ccc_linreg.fit(X, y)

# Answer check
print(ccc_linreg)
print(type(ccc_linreg))
print(ccc_linreg.coef_)

## Problem 8

### Interpreting the results
'''
**4 Points**

Examine the coefficients from the model and use them to determine the predicted price of a diamond with the following features:

```
carat = 0.8
cut = Ideal
clarity = SI2
```

Assign your solution as a float rounded to two decimal places to the variable `ccc_prediction` below.  
'''

ccc_prediction = 0.0
# Base price (intercept is zero since fit_intercept=False)
base_price = 0.0
# Add carat contribution
carat_col = 'carat_0.8'
if carat_col in X.columns:
    carat_index = X.columns.get_loc(carat_col)
    base_price += ccc_linreg.coef_[carat_index]
# Add cut contribution
cut_col = 'cut_Ideal'   
if cut_col in X.columns:
    cut_index = X.columns.get_loc(cut_col)
    base_price += ccc_linreg.coef_[cut_index]
# Add clarity contribution
clarity_col = 'clarity_SI2' 
if clarity_col in X.columns:
    clarity_index = X.columns.get_loc(clarity_col)
    base_price += ccc_linreg.coef_[clarity_index]
ccc_prediction = round(base_price, 2)   

# Answer check
print(f'Predicted price for carat 0.8, cut Ideal, clarity SI2: {ccc_prediction}')

## Problem 9

### A Model with all features
'''
**4 Points**

Use the `get_dummies()` function to create a dummy encoded version of all the columns in the `diamonds` DataFrame except for the column `price` and assign the result to the variable `X`.

To the variable `y`, assign the column `price` in the `diamonds` dataset.

Use the `LinearRegression` estimator  with argument `fit_intercept = False` to build a regression model. Next, use the `fit()` function with arguments `X` and `y`  to predict the `price` column.  

Assign the model to `all_features_linreg` below. 

Use the `mean_squared_error` function to compute the MSE between `all_features_linreg.predict(X)` and `y`. Assign the result to `linreg_mse` below. 
'''

X = pd.get_dummies(diamonds.drop(columns=['price']), drop_first=True)
y = diamonds['price']
all_features_linreg = LinearRegression(fit_intercept=False)
all_features_linreg.fit(X, y)
linreg_mse = mean_squared_error(y, all_features_linreg.predict(X))
# Answer check
print(all_features_linreg)
print(type(all_features_linreg))
print(f'Mean Squared Error: {linreg_mse}')


