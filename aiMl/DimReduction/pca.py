from scipy.linalg import svd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_olivetti_faces, fetch_california_housing
from sklearn.datasets import make_regression
from sklearn.datasets import fetch_openml

'''Both datasets are built into the `sklearn` library.  The first is a familiar set of faces, such as 1-Dimensional Arrays, and the second is a dataset on housing prices in Californian neighborhoods.  The image data is limited to a single image and assigned to the variable `image` below.  The housing data is displayed as a DataFrame with the `.frame` attribute after setting `as_frame = True`.  '''

faces_data = pd.read_csv('aiMl/DimReduction/data/faces.csv')
cali_housing = fetch_california_housing(return_X_y=False, as_frame=True, data_home='data')

image = faces_data.iloc[4].values.reshape(64, 64)
plt.imshow(image)

df = cali_housing.frame.head(5)
df.head()

### Principal Component Analysis 
'''
Recall the steps to perform Principal Component Analysis on an array.  

```
- standardize the data
- perform SVD
- select how many components to keep
```

From here, depending on the goal, you will either eliminate all but the top `r` values in $\Sigma$ or evaluate the product of $U_r \dot \Sigma_r$.'''

## Problem 1

### Function to Standardize and Factor
'''
**4 Points**

Complete the function `svd_norm` according to the instructions below:

- The function should take, as input, an array `X`.
- The function should scale the array `X` using its mean and standard deviation and assign the result to ` x_norm`.
- The function should use the `svd` function to factor `x_norm` using `full_matrices` equal to `False` and assign the result to `U`, `sigma`, and `VT`.
- The function should use `np.diag()` to define a diagonal matrix with the singular values on the main diagonal and assign the result to `Sigma`.
- The function should return three arrays `U`, `Sigma` and `VT`.
'''

def svd_norm(X):
    """This function takes in an array X, scales it according 
    to the transformation X - mu / sigma where mu is the mean
    and sigma the standard deviation of the dataset.

    Parameters
    ----------
    X: type `np.array`, shape (N, M)
        
    Returns
    -------
    A tuple (U, Sigma, VT) where
        U: type `np.ndarray`, shape (N, M)
            Numpy arrays with N rows, M columns 
        Sigma: type `np.ndarray`, shape (M, M)
            Numpy arrays with M rows and M columns
            A Diagonal matrix with the singular values on main diagonal
        VT: type `np.ndarray`, shape (M, M)
            Numpy array with M rows and M columns representing V Transpose
    """
    # Standardize the data
    mu = np.mean(X)
    sigma = np.std(X)
    x_norm = (X - mu) / sigma

    # Perform SVD
    U, singular_values, VT = svd(x_norm, full_matrices=False)

    # Create diagonal matrix Sigma
    Sigma = np.diag(singular_values)

    return U, Sigma, VT


# YOUR CODE HERE

# Answer check
U, Sigma, VT = svd_norm(image)
print(U.shape, Sigma.shape, VT.shape)

## Problem 2

### Reconstructing the Image
'''
**4 Points**

To complete this problem, follow the instructions below:

- Apply the `svd_norm` function you defined in Problem 1 to `image` and assign the result to `U`, `Sigma`, and `VT`.
- Use the `np.copy` function with argument `Sigma` to make a copy of the $\Sigma$ matrix and assign  the result to `Sigma_copy`.
- Set all but the first 5 singular values of `Sigma_copy` (first 25 values - 5x5 matrix) to zero.
-  Reconstruct the original image by multiplying $U \Sigma_{copy} VT$ with the `@` operator and assign the result to `simpler_image`. 

Note how much information from the image is captured in the first five singular values!
'''
Sigma_copy = None
simpler_image = None

# YOUR CODE HERE
U, Sigma, VT = svd_norm(image)
Sigma_copy = np.copy(Sigma) 
Sigma_copy[5:, 5:] = 0
simpler_image = U @ Sigma_copy @ VT

# Answer check
print(simpler_image.shape)
plt.imshow(simpler_image)
plt.title('Image Reconstructed from first 5 Singular Values')


### Problem 3
### Repeat for Tabular Data
'''
**4 Points**

As the example above demonstrates, using Principal Component Analysis is a way of extracting important information from the data through the SVD.  Now, you are to extract the matrix factorization from the SVD using the housing data `df`.  The earlier `svd_norm` function should work to factor a DataFrame.  Use your function to extract $U, \Sigma, VT$ from the DataFrame.  Assign your results to `U, Sigma, VT` below.
'''
U, Sigma, VT = None, None, None

# YOUR CODE HERE
df = cali_housing.frame
U, Sigma, VT = svd_norm(df.values)

# Answer check
print(type(U))
print(df.shape, Sigma.shape)

## Problem 4

## Function to project into lower dimension `r`
'''
**4 Points**

Complete the function `pca` below according to the instructions below:

- The function takes two arguments, `X` and `r` where `X` is an array or DataFrame and `r` is a dimension to project the data down into.
- The function should scale the array `X` using its mean and standard deviation and assign the result to ` x_norm`.
- The function should use the `svd` function to factor `x_norm` using `full_matrices` equal to `False` and assign the result to `U`, `sigma`, and `VT`.
- The function should use `np.diag()` to define a diagonal matrix with the singular values on the main diagonal anfd assign the result to `Sigma`.
- The function should extract all the rows and the first `r` columns of `U` and assign the result to `Ur`.
- The function should extract the first `r` rows and columns of `Sigma` and assign the result to `Sigma_r`.
- The function should returns a DataFrame of shape `(N, r)` with columns labeled `pca_1`, `pca_2`, ..., `pca_r`. To achieve this use the code `pd.DataFrame(Ur @ Sigma_r, columns = [f'pca_{i}' for i in range(1, r + 1)])`
'''

def pca(X, r = 5):
    """This function takes in an array X, and extracts
    r principal components.  These are returned in a DataFrame.

    Parameters
    ----------
    X: type `np.array`, shape (N, M)
    r: type `int`
        
    Returns
    -------
    A DataFrame of shape (N, r) with columns labeled
    pca_1. | pca_2 | .... | pca_r |
    
    """
    # Standardize the data
    mu = np.mean(X)
    sigma = np.std(X)
    x_norm = (X - mu) / sigma

    # Perform SVD
    U, singular_values, VT = svd(x_norm, full_matrices=False)

    # Create diagonal matrix Sigma
    Sigma = np.diag(singular_values)

    # Extract first r components
    Ur = U[:, :r]
    Sigma_r = Sigma[:r, :r]

    # Return DataFrame with principal components
    return pd.DataFrame(Ur @ Sigma_r, columns=[f'pca_{i}' for i in range(1, r + 1)])

# Answer check
XT = pca(df, r = 2)
print(XT.shape)
XT.head()

## Problem 5

### Extracting $\Sigma$
'''
**2 Points**

Complete the function `singular_values` according to the instructions below:

- The function takes, as input, an aray `X`, and a booloean flag `scale`, describing whether you want to scale the array `X` or not.
- Using an `if` statement, check if `scale` is `True`. If it is, scale `X` using its mean and standard deviation.
- If `scale` is not `True`, use the `svd` function to factor `X` into  `u`, `sigma`, and `vt`.
- The function should return the numpy array of singular values of X, `sigma`.
'''
def singular_values(X, scale = False):
    """Return the singular values resulting from 
    SVD decomposition.  

    Parameters
    ----------
    X: np.array or pd.DataFrame
        An array of data
    scale: boolean
        Boolean determines whether data needs to be scaled

    Returns an numpy array of singular values of X
    """
    if scale:
        mu = np.mean(X)
        sigma = np.std(X)
        x_norm = (X - mu) / sigma
        _, singular_values, _ = svd(x_norm, full_matrices=False)
    else:
        _, singular_values, _ = svd(X, full_matrices=False)
    
    return singular_values

# Answer check
print(type(singular_values(df)))
sigma = singular_values(df)
print(sigma.shape)

### Problem 6
### Plotting $\Sigma$
'''
**1 Points**

Using the function above, build a plot of the singular values. Use your plot to determine how many principal components you should keep from the DataFrame `df`.  Assign your solution as an integer to `ans2` below.'''

#plot of singular values here
singular_vals = singular_values(df, scale=True)
plt.figure(figsize=(8, 5))
sns.lineplot(x=np.arange(1, len(singular_vals) + 1), y=singular_vals, marker='o')
plt.title('Singular Values of the California Housing Data')
plt.xlabel('Index')
plt.ylabel('Singular Value')
plt.show()

# Based on the plot, we are looking for the "elbow" where the curve flattens out.
# This indicates the point at which subsequent principal components contribute
# significantly less variance explained. Looking at the plot, there is a clear
# elbow after the first two singular values, with a noticeable drop-off in magnitude.
# The curve then flattens out significantly. Therefore, keeping the first
# two principal components appears to be a reasonable choice.

#how many components should you keep?
ans2 = 2

#fetching the data
housing = fetch_openml(name="house_prices", as_frame=True, data_home='data')

#examine the dataframe
housing.frame

#select numeric data and drop missing values
df = housing.frame.select_dtypes(['float', 'int']).dropna(axis = 1)#.select_dtypes(['int', 'float'])

## Problem 7

### Scale the data
'''
**2 Points**

Scale the `df` data using its mean and standard deviation so that it is ready for SVD.  Assign the scaled data to `df_scaled` below.  
'''
mu = np.mean(df)
sigma = np.std(df)
df_scaled = (df - mu) / sigma
# Answer check
print(type(df_scaled))
print(df_scaled.describe())

## Problem 8
### Extracting $\Sigma$
'''
**2 Points**

Using the scaled data, extract the singular values from the data using the `scipy.linalg` function `svd`.  Assign your results to `U`, `sigma`, and `VT` below. 
'''

U, sigma, VT = svd(df_scaled.values, full_matrices=False)
# Answer check
print(type(sigma))
print(sigma.shape)

## Problem 9
### Percent Variance Explained
'''
**2 Points**

Divide `sigma` by the sum of the singular values to compute the percent variance explained. Assign your result as a percent array to `percent_variance_explained` below.  

Note that due to rounding this percent won't sum to exactly 1.  
'''

percent_variance_explained = sigma / np.sum(sigma)
print(percent_variance_explained.shape)
print(percent_variance_explained.sum())

## Problem 10

### Cumulative Variance Explained
'''
**3 Points**

Using the solution to problem 10, how many principal components are necessary to retain up to 80% of the explained variance if we consider them in descending order?  Assign your response to `ans11` below as an integer. 

**HINT**: explore the `np.cumsum` function.
'''
cumulative_variance_explained = np.cumsum(percent_variance_explained)
ans11 = np.argmax(cumulative_variance_explained >= 0.8) + 1  # +1 because indices start at 0    

print(type(ans11))
print(ans11)