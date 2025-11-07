'''
This assignment introduces the `Ridge` regression estimator from scikit-learn.  You will revisit the insurance data from the previous assignment and experiment with varying the `alpha` parameter discussed in Video 9.4. Your work here is a basic introduction where complexity in the preprocessing steps will be added to scale your data.  For now, you are just to familiarize yourself with the `Ridge` regression estimator and its `alpha` parameter. 
'''
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn import set_config
set_config(display="diagram")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

### The Data: Insurance
'''
Below the insurance data is loaded as train and test data with the cubic polynomial features created already.  Similarly, the transformed target feature is attached. 
'''
train_df = pd.read_csv('aiMl/seqFeatureSelection/data/train_cubic.csv')
test_df = pd.read_csv('aiMl/seqFeatureSelection/data/test_cubic.csv')

print(train_df.head())
print(test_df.head())

### Problem 1

#### Train and Test data
'''
**5 Points**

Use the `train_df` and `test_df` data to split the data into `X_train`, `X_test`, `y_train` and `y_test`.

Remember that the `target_log` column is the target column for your model.
'''
X_train, X_test, y_train, y_test = None, None, None, None
# YOUR CODE HERE
X_train = train_df.drop(columns=['target_log'])
X_test = test_df.drop(columns=['target_log'])
y_train = train_df['target_log']
y_test = test_df['target_log']
# END YOUR CODE

# Answer check
print(type(X_train))
print(type(y_train))

### Problem 2
#### Default `Ridge` model
'''
**10 Points**

Now, use the `Ridge` regressor with default settings to build your first model. To this regressor, chain a `fit()` function to  train your model using `X_train` and `y_train`. Assign the result to `model_1`.

Next, assign `model_1` coefficients as an array to `model_1_coefs` below.  
'''

# YOUR CODE HERE
model_1 = Ridge().fit(X_train, y_train)
model_1_coefs = model_1.coef_   
# END YOUR CODE

# Answer check
print(f'Ridge Coefs: {np.round(model_1_coefs, 2)}')

### Problem 3

#### Exploring different `alpha` values
'''
**10 Points**

Below, a list of alpha values is given to you. Define a `for` loop to iterate over the list `alphas` to create and train different Ridge models.

Append the coefficients of each Ridge model as a list to `coef_list` below.  
'''
alphas = [0.001, 1.0, 10.0, 100.0]
coef_list = []
# YOUR CODE HERE
for alpha in alphas:
    model = Ridge(alpha=alpha).fit(X_train, y_train)
    coef_list.append(model.coef_)
# END YOUR CODE

# Answer check
len(coef_list)
print('For alpha = 100 we have the following coefficients:')
list(zip(X_train.columns, coef_list[-1]))

### Problem 4

#### Exploring the coefficient for `children`
'''
**5 Points**

To see the effect of varying alpha, you are to focus on the coefficients of the `children` feature.  Use the code `list([i[2] for i in coef_list])` to assign those values as a list to `child_coefs` below, building models on the given list of alphas.   

In general, as you increase `alpha` what happens to the value of the coefficient -- `increase`, `decrease`, or `neither`?  Assign your answer as a string to `ans4` below. 
'''
child_coefs = None
ans4 = None

# YOUR CODE HERE
child_coefs = list([i[2] for i in coef_list])
ans4 = 'decrease'
# END YOUR CODE

# Answer check
print(f'Children Coefficients: {child_coefs}')
print(f'Answer: {ans4}')