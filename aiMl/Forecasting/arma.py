### ACF and PACF Plots for ARMA Models
'''
This assignment focuses on using the autocorrelation and partial autocorrelation plots to determine parameters for stationary data.  In general, you will first determine the stationarity of a time series using the Dickey-Fuller test (or eyeballing it) and then examine the autocorrelation and partial autocorrelation to identify the parameters for each term.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

### The Data
'''
Two datasets are used to examine stationarity and autoregression and moving average components for ARMA models.  The first is the recruits data encountered earlier.  The second is a series of Quarterly GNP data from the United States from 1947 through 2002. In the first, you predict the number of recruits, and in the second, your target is the difference of the logarithm of the GNP. 
'''

recruits = pd.read_csv('aiMl/Forecasting/Data2/recruitment.csv', index_col=0)
print(recruits.head())
plt.plot(recruits.values)
plt.grid()
plt.title('Recruits Data')
plt.show()

### Problem 1

#### Is it Stationary? 
'''
**10 Points**

As discussed, our ARMA models are only applicable to stationary data.  Use the `adfuller` function to determine if the recruits data is stationary at the 0.05 level.  Assign your answer as a string to `ans1` below.  
'''
result = adfuller(recruits.values)
if result[1] < 0.05:
    ans1 = "yes"
else:
    ans1 = "no"

# Answer check
print(f"Is the recruits data stationary? {ans1}")

### Problem 2

#### Building train and test set
'''
**10 Points**

Now, we use the familiar `train_test_split` and set `shuffle = False` to create a temporal train and test set.  Leave all arguments to default except `shuffle`.  Assign your results as `y_hist` and `y_future` below. 
'''

y_hist, y_future = train_test_split(recruits, shuffle=False)

# Answer check
print("History\n=========")
print(y_hist.tail())
print("Future\n==========")
print(y_future.head())

### Problem 3

#### Examining acf and pacf
'''
**10 Points**

Below, the ACF and PACF plots are shown.  While the ACF plot isn't incredibly helpful, the PACF may suggest using a value of `p = 1` in an ARMA model.  As such, create and fit an ARIMA model with `p = 1` and `q = 1`.  Assign your fit model as `arma` below.
'''
fig, ax = plt.subplots(1, 2, figsize = (16, 5))
plot_acf(y_hist, ax = ax[0]);
ax[0].grid()
plot_pacf(y_hist, ax = ax[1], method = 'ywm');
ax[1].grid()
ax[0].show()
ax[1].show()

y_hist.index = pd.to_datetime(y_hist.index)
print(y_hist.info())

arma = ARIMA(y_hist, order=(1, 0, 1)).fit()


# Answer check
print("ARMA Model Summary\n===================")
print(arma.summary())

### Problem 4

#### Making Predictions
'''
**10 Points**

Use the `arma` object to make predictions for the training data.  Assign these results as `hist_preds` below.  Uncomment the code to view a plot of the results against the original series. 
'''

hist_preds = arma.predict(start=y_hist.index[0], end=y_hist.index[-1])


# Answer check
print(hist_preds.tail())
plt.figure(figsize = (12, 4))
plt.plot(hist_preds, label = 'model')
plt.plot(y_hist, label = 'data')
plt.legend()
plt.grid()
plt.title('Result of ARMA Model')
plt.show()

### Problem 5

#### Forecasting with the ARMA model
'''
**10 Points**

Finally, to use the forecasting capabilities of the model, pass the number of steps to forecast in the future.  Assign the forecast into the future to match up with `y_future` values as `future_preds` below.  
'''

y_future.index = pd.to_datetime(y_future.index)

future_preds = arma.forecast(steps=len(y_future))

# Answer check
print(future_preds.tail())
print(y_future.tail())

### Problem 6

#### The GNP series
'''
**10 Points**

Below, the `gnp` data is loaded and displayed.  This data is transformed according to the first difference of the logarithm so as to form a stationary series.  Then, the ACF and PACF plots are shown on the stationary series.  These suggest that an AR(2) and MA(2) model might be appropriate.  Build an `ARIMA` model on `y` and predict as `preds`.  Uncomment the code to visualize the predictions.
'''

gnp = pd.read_csv('data/gnp.csv', index_col=0)
gnp.index = pd.Index(pd.date_range("1947-Q1", "2002-Q4", freq = "Q"))
gnp.head()

gnp.plot()
plt.title('GNP Data')
plt.grid()
plt.show()

y = np.log(gnp).diff().dropna()
#note the stationarity
adfuller(y)

fig, ax = plt.subplots(1, 2, figsize = (14, 4))
plot_acf(y, ax = ax[0]);
ax[0].grid()
plot_pacf(y, ax = ax[1])
ax[1].grid()
ax[0].show()
ax[1].show()

arma2 = ARIMA(y, order=(2, 0, 2)).fit()
preds = arma2.predict(start=y.index[0], end=y.index[-1])


# # Answer check
plt.figure(figsize = (12, 4))
plt.plot(y, label = 'data')
plt.plot(preds, label = 'predictions')
plt.legend()
plt.grid()
plt.title('Result of ARMA Model')
plt.show()


### Problem 7

#### Errors and Autocorrelation
'''
**10 Points**

Below, subtract the predictions from the actual series.  Determine the stationarity of the results by examining the autocorrelation plot of the residuals.  Is there a structure remaining in the series based on this?  Assign your answer as a string to `ans7` below -- 'yes' or 'no'.
'''

preds = pd.DataFrame(preds)
preds.columns = ['value']

resids = y - preds
ans7 = 'yes'

# Answer check
plot_acf(resids)