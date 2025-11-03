import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import plotly.express as px

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

#### Iterate on Models
'''
**20 Points**

Complete the code below according to the instructions below:

- Assign the values in the `horsepower` column of `auto` to the variable `X` below.
- Assign the values in the `mpg` column of `auto` to the variable `y` below.

Use a `for` loop to loop over the values from one to ten. For each iteration `i`:

- Use `Pipeline` to create a pipeline object. Inside the pipeline object, define a a tuple where the first element is a string identifier `quad_features'` and the second element is an instance of `PolynomialFeatures` of degree `i` with `include_bias = False`. Inside the pipeline define another tuple where the first element is a string identifier `quad_model`, and the second element is an instance of `LinearRegression`. Assign the pipeline object to the variable `pipe`.
- Use the `fit` function on `pipe` to train your model on `X_train` and `y_train`. Assign the result to `preds`.
- Use the `predict` function to predict the value of `X_train`. Assign the result to `preds`.
- Assign each `model_predictions` of degree `i` the corresponding `preds` value.
'''

model_predictions = {f'degree_{i}': None for i in range(1, 11)}

print("Starting Dictionary of Predictions\n", model_predictions)
for i in range(1, 11):

    #create pipeline
    pipe = Pipeline([
        ('quad_features', PolynomialFeatures(degree=i, include_bias=False)),
        ('quad_model', LinearRegression())
    ])
    
    #fit pipeline on training data
    pipe.fit(X_train, y_train)

    #make predictions on all data
    preds = pipe.predict(X_train)
    
    #assign to model_predictions
    model_predictions[f'degree_{i}'] = preds


# Answer check
print(model_predictions['degree_1'][:10])

### Problem 2

#### DataFrame of Predictions
'''
**5 Points**

Use the `model_predictions` dictionary to create a DataFrame of the 10 models predictions.  Assign your solution to `pred_df` below as a DataFrame. 
'''

pred_df = pd.DataFrame(model_predictions)

# Answer check
print(pred_df.head())

### Problem 3

#### DataFrame of Errors
'''
**5 Points**

Now, determine the error for each model and create a DataFrame of these errors.  One way to do this is to use your prediction DataFrame's `.subtract` method to subtract `y` from each feature.  Assign the DataFrame of errors as `error_df` below.  
'''

error_df = pred_df.subtract(y, axis=0)

# Answer check
print(error_df.head())

### Problem 4

#### Mean and Variance of Model Errors
'''
**5 Points**


Using the DataFrame of errors, examine the mean and variance of each model's error.  What degree model has the highest variance?  Assign your response as an integer to `highest_var_degree` after computing the variance_errors using `.var()` and assigning it to `variance_errors()`.

HINT: Use `int(variance_errors.idxmax().split('_')[1])` to get the integer output of the degree. 
'''
variance_errors = error_df.var()
highest_var_degree = int(variance_errors.idxmax().split('_')[1])

# Answer check
print(variance_errors)
