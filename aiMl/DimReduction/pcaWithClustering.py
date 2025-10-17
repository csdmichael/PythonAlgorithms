import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")

'''
The Dataset
More information on the dataset can be found here. Below, the data is loaded, the info is displayed, the continuous features are described, and the first five rows of the data are displayed
'''
df = pd.read_csv('aiMl/DimReduction/data/marketing_campaign.csv', sep = '\t')
df.info()
df.describe()
df.head()

## Problem 1

### Preparing the Data
'''
**4 Points**

Before starting to build cluster models, the data needs to be limited to numeric representations.  How many non-numeric columns are there, and what are their names?  Assign your solution as a list of strings to `object_cols` below.  The names should match the column names in the DataFrame exactly.  
'''
object_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"Non-numeric columns ({len(object_cols)}): {object_cols}")

## Problem 2

### Dropping the `object` columns 
'''
**4 Points**

To simplify things, eliminate the columns containing `object` datatypes.  Assign your new DataFrame to `df_numeric` below.
'''
df_numeric = df.select_dtypes(exclude=['object'])
print(df_numeric.shape)
df_numeric.info()

## Problem 3   
### Dropping non-informative columns
'''
**4 Points**

Two columns, `Z_CostContact`, and `Z_Revenue` have one unique value. Also, the `ID` column is basically an index. These will not add any information to our problem. Drop the columns `Z_CostContact`, `Z_Revenue`, and `ID` and save your all numeric data without these two columns as a DataFrame to `df_clean` below.
'''
df_clean = df_numeric.drop(columns=['Z_CostContact', 'Z_Revenue', 'ID'])
print(df_clean.shape)
df_clean.info()

## Problem 4

### Dropping the missing data
'''
**4 Points**

Note that the `Income` column is missing data.  This will cause issues for `PCA` and clustering algorithms.  Drop the missing data using pandas `.dropna` method on `df_clean`, and assign your non-missing dataset as a DataFrame to `df_clean_nona` below. 
'''
df_clean_nona = df_clean.dropna()
print(df_clean_nona.shape)
df_clean_nona.info()

## Problem 5

### Scaling the Data
'''
**4 Points**

As earlier with the PCA models, the data needs to be mean-centered.  


Below, scale the `df_clean_nona` by subtracting its mean and by dividing it by its standard deviation.  Assign your results as a DataFrame to `df_scaled` below.  
'''

df_scaled = pd.DataFrame(StandardScaler().fit_transform(df_clean_nona), columns=df_clean_nona.columns)
print(df_scaled.shape)
df_scaled.info()

## Problem 6

### PCA
'''
**4 Points**

With the data cleaned and scaled, you are ready to perform PCA.  Below, use the `PCA` transformer from `sklearn` to transform your data and select the top three principal components.  First, create an instance of the `PCA` that limits the number of components to 3 using the `n_components` argument.  Also, set the argument `random_state = 42`  and assign your instance as `pca` below.
'''

pca = PCA(n_components=3, random_state=42)
# Answer check
print(pca)
print(pca.n_components)

## Problem 7

### Extracting the Components
'''
**4 Points**

Use the `.fit_transform` method with an argument equal to `df_scaled` on `pca` to extract the three principal components.  Save these components as an array to the variable `components` below.  
'''
components = pca.fit_transform(df_scaled)
print(components.shape)

## Problem 8

### `KMeans`
'''
**4 Points**
Complete the code below according to the instructions below:


- To the `kmeans` variable, assign the `KMeans` clustered with the argument `n_clusters` equal to `3` and the argument `random_state` equal to `42`. To this, chain the `fit()` method with the argument equal to `components`.
- Copy the code line that reads the data  in your solution code.
- Copy the code to drop the missing value in your solution. Here, inside the `dropna()` function, set the argument `subset` equal to `['Income']`.
- Inside `df_clustered`, create a new column `cluster`. To this column, assign `kmeans.labels_`.
'''

kmeans = KMeans(n_clusters=3, random_state=42).fit(components)
df = pd.read_csv('data/marketing_campaign.csv', sep = '\t')
df_clustered = df.dropna()
df_clustered['cluster'] = kmeans.labels_

# Answer check
print(type(df_clustered))
print(df_clustered.shape)

## Problem 9

### Examining the Results
'''
**4 Points**

The image below shows a `boxenplot` of the clusters based on amounts spent on meat products.  If you were marketing a meat sale and there is a cost involved in advertisiting per customer.  If you were to select only one cluster to market to, which cluster would you target? Assign your response as an integer to `target_cluster` below.
'''
target_cluster = 2

# Answer check
print(type(target_cluster))
print(target_cluster)