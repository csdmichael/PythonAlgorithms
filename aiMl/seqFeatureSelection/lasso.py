'''
This assignment introduces the `Ridge` regression estimator from scikitlearn.  You will revisit the insurance data from the previous assignment and experiment with varying the `alpha` parameter discussed in Video 9.4. Your work here is a basic introduction where complexity in the preprocessing steps will be added to scale your data.  For now, you are just to familiarize yourself with the `Ridge` regression estimator and its `alpha` parameter. 

This assignment compares a second regularized regression method -- the LASSO -- with that of sequential feature selection.  The LASSO will be briefly discussed below, and you will use the scikit learn implementation.  Rather than using the LASSO as a model, you are to compare it to the `SequentialFeatureSelection` transformer as a method to select important features for a regression model. 
'''
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SequentialFeatureSelector, SelectFromModel
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import set_config
set_config(display="diagram")


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

### The Data
'''
For this exercise, you will revisit the automotive data.  The goal is again to predict the `mpg` column using the other numeric features.  You will build a polynomial model of degree 3 to compare the results of a `Lasso` and that of a `LinearRegression` model. Finally, you will use the `Lasso` estimator to select features in a pipeline with `SelectFromModel`. 

Below, the train and test data is created for you as `auto_X_train`, `auto_X_test`, `auto_y_train`, and `auto_y_test`.
'''

auto = pd.read_csv('aiMl/seqFeatureSelection/data/auto.csv')
print(auto.head())

#generate train/test data for auto
auto_X = auto.drop(['mpg', 'name'], axis = 1)
auto_y = auto['mpg']
auto_X_train, auto_X_test, auto_y_train, auto_y_test = train_test_split(auto_X, auto_y, 
                                                                       test_size = 0.3,
                                                                       random_state = 42)

### Problem 1
#### The auto data
'''
**10 Points**

To start, build a `Pipeline` named `auto_pipe` with named steps `polyfeatures`, `scaler` and `lasso` model that utilizes `PolynomialFeatures`, `StandardScaler`, and the `Lasso` estimator with the following parameters:

- `degree = 3` in `PolynomialFeatures`
- `include_bias = False` in `PolynomialFeatures`
- `random_state = 42` in `Lasso`

Fit the pipeline on `auto_X_train` and `auto_y_train` data given.  Extract the lasso coefficients from the pipeline and assign them as an array to `lasso_coefs` below.  

**HINT**: Use the `.named_steps['lasso']` to extract that lasso estimator and use the `.coef_` attribute after fitting to access the model coefficients.
'''

auto_pipe = Pipeline(steps=[
    ('polyfeatures', PolynomialFeatures(degree=3, include_bias=False)),
    ('scaler', StandardScaler()),
    ('lasso', Lasso(random_state=42))
])
auto_pipe.fit(auto_X_train, auto_y_train)
lasso_coefs = auto_pipe.named_steps['lasso'].coef_

# Answer check
print(lasso_coefs)
print(len(lasso_coefs))
print  (auto_pipe)

### Problem 2

#### Error in `Lasso` model
'''
**10 Points**

Now, compute the mean squared error of the LASSO model on both the train and test data, `auto_X_train` and `auto_X_test`, respectively.  Assign this as a float to `lasso_train_mse` and `lasso_test_mse` respectively.  
'''

auto_y_train_pred = auto_pipe.predict(auto_X_train)
auto_y_test_pred = auto_pipe.predict(auto_X_test)
lasso_train_mse = mean_squared_error(auto_y_train, auto_y_train_pred)
lasso_test_mse = mean_squared_error(auto_y_test, auto_y_test_pred)

# Answer check
print(lasso_train_mse)
print(lasso_test_mse)

### Problem 3

#### Non-zero coefficients
'''
**10 Points**

Using the `lasso_coefs` determine the number of features with non-zero coefficients and determine the name of those features as a result of the polynomial feature transformation.  

To do this, access the `named_steps['polyfeatures']` feature from the `auto_pipe` pipeline and chain the `get_feature_names_out()` to get the features name. Assign the result to `feature_names`.

Next, create a DataFrame named `lasso_df` below that has two columns -- `feature` and `coef`.  To the `feature` column assign `feature_names`. To the `coef` column assign `lasso_coefs`.
'''

feature_names = auto_pipe.named_steps['polyfeatures'].get_feature_names_out()
lasso_df = pd.DataFrame({
    'feature': feature_names,
    'coef': lasso_coefs
})

# Answer check
print(lasso_df.head())
print(lasso_df[lasso_df['coef'] != 0])

### Problem 4

#### Comparing `Lasso` to `SequentialFeatureSelection`
'''
**10 Points**

As seen above, the Lasso model effectively eliminated all but 6 features from the cubic polynomial example.  Now, you are to build a `Pipeline` object called `sequential_pipe` with named steps `poly_features`, `selector`, and `linreg` with `PolynomialFeatures`, `SequentialFeatureSelector`, and `LinearRegression` respectively that uses the following parameters:

- `degree = 3` in `PolynomialFeatures` step `poly_features`
- `include_bias = False` in `PolynomialFeatures` step `poly_features`
- `n_features_to_select = 6` in `selector`

Assign this pipeline object to `sequential_pipe`.

Next, use the `fit` function on `scaled_pipe` to train your model on `auto_X_train` and `auto_y_train`. 

Use the `mean_squared_error` function to compute the MSE between `auto_y_train` and` sequential_pipe.predict(auto_X_train)`. Assign your result to `sequential_train_mse`.

Use the `mean_squared_error` function to compute the MSE between `auto_y_test` and `sequential_pipe.predict(auto_X_test)`. Assign your result to `sequential_test_mse`.
'''

sequential_pipe = Pipeline(steps=[
    ('poly_features', PolynomialFeatures(degree=3, include_bias=False)),
    ('selector', SequentialFeatureSelector(LinearRegression(), n_features_to_select=6)),
    ('linreg', LinearRegression())
])

sequential_pipe.fit(auto_X_train, auto_y_train)
sequential_train_mse = mean_squared_error(auto_y_train, sequential_pipe.predict(auto_X_train))
sequential_test_mse = mean_squared_error(auto_y_test, sequential_pipe.predict(auto_X_test))

# Answer check
print(sequential_train_mse)
print(sequential_test_mse)

### Problem 5

#### Using `Lasso` as a feature selector
'''
**10 Points**

Rather than using the `Lasso` as the estimator, you can use the results of the `Lasso` to select features that are subsequently used in a `LinearRegression` estimator.  To do so, scikitlearn provides a function in the `feature_selection` module called `SelectFromModel` that will select the features based on coefficients.  

As such, using the `Lasso` estimator to select features would involve instantiating the `SelectFromModel` transformer and selecting features as:

```python
selector = SelectFromModel(Lasso())
selector.transform(auto_X_train)
```
'''

model_selector_pipe = Pipeline([('poly_features', PolynomialFeatures(degree = 3, include_bias = False)),
                                ('scaler', StandardScaler()),
                                ('selector', SelectFromModel(Lasso())),
                                    ('linreg', LinearRegression())])

model_selector_pipe.fit(auto_X_train, auto_y_train)
model_selector_train_mse = mean_squared_error(auto_y_train, model_selector_pipe.predict(auto_X_train))
model_selector_test_mse = mean_squared_error(auto_y_test, model_selector_pipe.predict(auto_X_test))

# Answer check
print(model_selector_train_mse)
print(model_selector_test_mse)

