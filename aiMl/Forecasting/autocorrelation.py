'''
This activity focuses on computing the autocorrelation of a time series dataset. You will use statsmodels to compute autocorrelation and determine whether or not the series is stationary. Finally, you are to difference the data and see if the resulting series is itself stationary.
'''
import numpy as np
import pandas as pd
from statsmodels.tsa import arima_process
import matplotlib.pyplot as plt
import warnings

from statsmodels.datasets import nile
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import acf
warnings.filterwarnings("ignore")

### Problem 1
'''
**10 Points**

#### Creating a dataset with `ArmaProcess`

Following video 10.3, create an `arima_process` using the arguments:

- `ar = [.9, -0.3]`
- `ma = [2]`

Assign this as an `ArmaProcess` object to `process` below.
'''

ar = np.array([0.9, -0.3])  # Note the sign change for statsmodels
ma = np.array([2])
process = arima_process.ArmaProcess(ar, ma)

# Answer check
print(process)

### Problem 2
'''
**10 Points**

#### Generating a sample

<center>
    <img src = images/arma1.png/>
</center>


Next, you are to generate a sample of size 100 from the arima_process created in [Problem 1](#Problem-1).  To assure consistent results, make sure to leave the `np.random.seed(32)`.  This assures the same sample will be generated time after time.
'''

np.random.seed(32)#dont

sample = process.generate_sample(nsample=100)

### Answer check
print(sample[:5])


## Uncomment to plot the sample
plt.plot(sample, '--o')
plt.title('Arma Process Sample Data')
plt.grid()
plt.show()

### Problem 3
'''
**10 Points**


#### Computing the autocorrelation

Use the `sample` created above together with the `acf` function from statsmodels to compute the autocorrelation values for the sample.  Assign these values to `auto_corr` as an array below.  **Note**: Set `fft = True` in the acf function to avoid a warning.

<center>
    <img src = 'images/arma2.png'/>
</center>
'''

auto_corr = acf(sample, fft=True)

# Answer check
print(auto_corr)

### Problem 4
'''
**10 Points**

#### Using `acf` to compute autocorrelation

Below, a dataset relating the volume of flow in the Nile River from statsmodels is loaded  and visualized.  Use the `acf` function from statsmodels to compute the autocorrelation values of the `volume` feature. Assign your results as an array to `nile_acf` below.  

Visualizing the autocorrelation data using the `plot_acf` function from statsmodels generates:

<center>
    <img src = 'images/ar4.png' />
</center>

Does this suggest the data is stationary?  Why or why not?
'''

nile_df = nile.load_pandas().data
print(nile_df.head())

plt.plot(nile_df['year'], nile_df['volume'], '--o')
plt.title('Nile River flows at Ashwan 1871 - 1970.')
plt.grid()
plt.show()

nile_acf = acf(nile_df['volume'], fft=True)

# Answer check
print(nile_acf[:5])

### Problem 5
'''
**10 Points**

#### Tesla and stationarity

Below, stock data from Tesla corporation are loaded from the beginning of the year 2020.  The Adjusted Closing price is plotted below.  You are to use the autocorrelation plots to determine which version of the data is stationary.  Assign one of the following strings to `ans5` below:

- `original`: the original adjusted closing price is stationary
- `first_diff`: the first difference of the adjusted closing price is stationary
- `neither`: neither the original time series or its first difference are stationary
'''

tsla = pd.read_csv('aiMl/Forecasting/data/TSLA.csv', index_col='Date')
print(tsla.head())
plt.plot(tsla['Adj Close'])
plt.grid()
#plt.xticks(rotation = 40)
plt.title('TSLA Adjusted Closing Price 2020 - 2021')
plt.show()

ans5 = 'first_diff'  # replace None with your answer