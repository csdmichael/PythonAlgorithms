'''
This activity is meant to extend your work with ARMA models to apply a forecasting model across stores in a retail chain, and items in each store. You will build models for each store for a specific item and compare this forecast to the model, aggregating all stores. Also, you will compare a model for sales by store for all items and discuss expected performance for each store according to your forecast.

In addition to the ARMA models, you will explore an extension of this to include seasonality elements with the SARIMA model. Both are implemented with statsmodels.
'''
### The Data
'''
The data is from a past time series competition on Kaggle [here](https://www.kaggle.com/c/demand-forecasting-kernels-only).  It represents historical sales across 10 stores of 50 items.  Each observation is a day's total sales by store and item.  
'''
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from warnings import filterwarnings 
filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import mean_squared_error

df = pd.read_csv('aiMl/Forecasting/data/train.csv.zip', compression = 'zip')
print(df.head())

### Problem 1

#### Structuring the data and time series
'''
**5 Points**

To begin, notice that the DataFrame `df` does not have a datetime index.  Below, convert the `date` column to a datetime object and set it as the index to a new DataFrame called `stores_df` below.
'''
stores_df = df.set_index(pd.to_datetime(df['date'])).drop('date', axis = 1)

# Answer check
print(stores_df.head())
print('------------\nData Info\n')
print(stores_df.info())

### Problem 2

#### Store 1 Model
'''
**10 Points**

In anticipation of building a 30-day forecast for sales of item 1 in store 1, subset the data to only the sales column for item 1 store 1 and assign as a DataFrame to `store_1_item_1` below. 
'''

store_1_item_1 = stores_df[(stores_df['store'] == 1) & (stores_df['item'] == 1)][['sales']]

# Answer check
print(store_1_item_1.head())

### Problem 3

#### Train/Test split
'''
**5 Points**

Now, use the store 1 data from the previous question to create a train-test split where `train_data` is all but the last 30 days of sales data.  You no longer need the store and item columns.  Assign these values as `X_train` and `X_test` respectively.
'''
X_train, X_test = store_1_item_1.iloc[:-30], store_1_item_1.iloc[-30:]

# Answer check
print(X_train.tail())
print(X_test.head())

### Problem 4

#### Assumptions of Linearity
'''
**10 Points**

Next, you will want to check the assumptions of our model before building it.  Specifically, this was the notion that our time series is stationary for the ARMA models.  Use the `adfuller` function to determine if the series is stationary.  Assign the $p$ value to `pval` below.  Consider your threshold at $p = 0.01$.  
'''

pval = adfuller(X_train)[1]

# Answer check
print(f'The p-value is {pval: .4f}')



### Problem 5

#### Autocorrelation and Partial Autocorrelation
'''
**10 Points**

Backing up the results of our hypothesis test, the autocorrelation of the original series 
seems to not be stationary.  Instead, the differenced data and its ACF and PACF plot look better.  
We will begin by using these plots to suggest an `order = (1, 0, 1)` model based on the differenced data.  
Accordingly, build an `ARIMA` model with `order = (1, 0, 1)` and fit on the training data and assign to `arma` below.

Determine the mean squared error on the test data and assign as a float to `mse_test` below.  
'''

fig, ax = plt.subplots(1, 4, figsize = (20, 5))
plot_acf(df[(df['store'] == 1) & (df['item'] == 1)]['sales'], ax = ax[0]);
ax[0].set_title('Original Series Autocorrelation')
plot_acf(df[(df['store'] == 1) & (df['item'] == 1)]['sales'].diff().dropna(), ax = ax[1]);
ax[1].set_title('Differenced Autocorrelation')
plot_pacf(df[(df['store'] == 1) & (df['item'] == 1)]['sales'].diff().dropna(), ax = ax[2], method = 'ywm');
ax[3].plot(df[(df['store'] == 1) & (df['item'] == 1)]['sales'].diff().dropna())
ax[3].set_title('Differenced Sales Series')

plt.show()

### BEGIN SOLUTION
arma = ARIMA(X_train.diff(), order = (1, 0, 1), freq = 'D').fit()
preds = arma.forecast(len(X_test))
mse_test = mean_squared_error(preds, X_test)
### END SOLUTION

### ANSWER CHECK
print(preds[:5])
print(mse_test)

plt.plot(arma.forecast(steps = len(X_test)), label = 'forecast')
plt.plot(X_test.diff(), label = 'Differenced Series')
plt.title('Comparing the Forecast')
plt.legend()
plt.xticks(rotation = 60)
plt.grid()

plt.show()

### Problem 6

#### A Model with Seasonality
'''
**10 Points**

As discussed with the decomposition models earlier, there are ways to consider a seasonal oscillation within the data.  For ARIMA a version that adds a seasonal element is called SARIMA.  In statsmodels, we use the `SARIMAX` estimator to build this model that includes seasonal elements.

Much like the decomposition model, you can have a multiplicative or additive seasonality.  For a multiplicative seasonal effect that we determine is yearly we add an argument

```
seasonal_order=(1, 1, 0, 12)
```

along with the `order = (1, 0, 1)`.  For more information see the user guide from statsmodels [here](https://www.statsmodels.org/dev/examples/notebooks/generated/statespace_sarimax_stata.html).

Below, build a `SARIMAX` estimator with the above order and seasonality and fit on the training data.  Assign the fit model to `sarima` below.
'''

print(stores_df.head())

X_train, X_test = stores_df['sales'].iloc[-700:-30], stores_df.iloc[-30:]

sarima = SARIMAX(X_train,  order=(1, 0, 1), seasonal_order=(1, 1, 0, 12)).fit(disp=0)

# Answer check
print(sarima.summary())

plt.plot(X_train.index, sarima.predict())
plt.plot(X_train.index, X_train, alpha = 0.3)
plt.xticks(rotation = 60)
plt.title('The SARIMA Model')
plt.grid()
plt.show()


