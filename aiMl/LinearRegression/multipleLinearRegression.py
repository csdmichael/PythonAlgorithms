import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

### The Dataset
'''
Below, a dataset containing information on diamonds is loaded and displayed.  Your task is to build a regression model that predicts the price of the diamond given different features as inputs.  
'''

diamonds = sns.load_dataset('diamonds')
print(diamonds.head())

## Problem 1

### Regression with single feature
'''
**5 Points**

Use sklearn's `LinearRegression` estimator with argument `fit_intercept` equal to `False` to build a regression model. Next, chain a `fit()` function using the `carat` column as the feature and the `price` column as the target.  

Assign your result to the variable `lr_1_feature` below.
'''
lr_1_feature = LinearRegression(fit_intercept=False)
features_1 = diamonds[['carat']]
target = diamonds['price']
lr_1_feature.fit(features_1, target)

# Answer check
print(lr_1_feature)

## Problem 2

### Regression with two features
'''
**5 Points**

Use sklearn's `LinearRegression` estimator with argument `fit_intercept` equal to `False` to build a regression model. Next, chain a `fit()` function using the `carat` and `depth` columns as the feature and the `price` column as the target.  

Assign your result to the variable `lr_2_feature` below.
'''
lr_2_feature = LinearRegression(fit_intercept=False)
features_2 = diamonds[['carat', 'depth']]
lr_2_feature.fit(features_2, target)

# Answer check
print(lr_2_feature)

## Problem 3
### Regression with three features
'''
**5 Points**

Use sklearn's `LinearRegression` estimator with argument `fit_intercept` equal to `False` to build a regression model. Next, chain a `fit()` function using the `carat`, `delth`, and `table` columns as the feature and the `price` column as the target.  

Assign your result to the variable `lr_3_feature` below.
'''
lr_3_feature = LinearRegression(fit_intercept=False)
features_3 = diamonds[['carat', 'depth', 'table']]
lr_3_feature.fit(features_3, target)
# Answer check
print(lr_3_feature)

## Problem 4

### Computing MSE and MAE
'''
**5 Points**

For each of your models, compute the mean squared error and mean absolute errors.  Create a DataFrame to match the structure below:

| Features | MSE | MAE |
| ----- | ----- | ----- |
| 1 Feature |  -  | - |
| 2 Features | -  | -  |
| 3 Features | - | - |

Assign your solution as a DataFrame to `error_df` below.  Note that the `Features` column should be the index column in your DataFrame.
'''

pred_1 = lr_1_feature.predict(features_1)
pred_2 = lr_2_feature.predict(features_2)
pred_3 = lr_3_feature.predict(features_3)
mse_1 = mean_squared_error(target, pred_1)
mae_1 = mean_absolute_error(target, pred_1)
mse_2 = mean_squared_error(target, pred_2)
mae_2 = mean_absolute_error(target, pred_2)
mse_3 = mean_squared_error(target, pred_3)
mae_3 = mean_absolute_error(target, pred_3)
error_data = {
    'Features': ['1 Feature', '2 Features', '3 Features'],
    'MSE': [mse_1, mse_2, mse_3],
    'MAE': [mae_1, mae_2, mae_3]
}
error_df = pd.DataFrame(error_data)
error_df.set_index('Features', inplace=True)
# Answer check
print(error_df)
