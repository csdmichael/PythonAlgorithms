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
    ans1 = "Yes"
else:
    ans1 = "No"

# Answer check
print(f"Is the recruits data stationary? {ans1}")
