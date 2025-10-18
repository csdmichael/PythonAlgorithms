import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv('aiMl/DataCleaning/data/biz.zip', compression = 'zip')
print(df.head())

### Problem 1

#### Plot of Missing Data
'''
**0 Points**

Create a barplot using `matplotlib` with the $x$-axis representing the columns and the $y$-axis representing the count of missing values. Sort these values from least to greatest.  Save your plot in the `images` folder as `missing_plot.png`.  
'''
# YOUR CODE HERE
missing_counts = df.isnull().sum()

# Sort the missing value counts from least to greatest
missing_counts_sorted = missing_counts.sort_values()

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(missing_counts_sorted.index, missing_counts_sorted.values)
plt.xticks(rotation=90)
plt.xlabel('Columns')
plt.ylabel('Count of Missing Values')
plt.title('Count of Missing Values per Column')
plt.tight_layout()
plt.savefig('aiMl/DataCleaning/images/missing_plot.png')
plt.show()

### Problem 2

#### `name` column
'''
**5 Points**

The column `name` has 31 missing values.

Subset the data to examine these observations where `name` is missing. Assign the result as a DataFrame to `ans2` below. 
'''

# YOUR CODE HERE
ans2 = df[df['name'].isnull()]
print(ans2)

### Problem 3
### Filling Missing Values in `name`
'''
**5 Points**

Examining the rows missing values in names shows that in the adjacent `a` column, the end of the URL contains what can stand in as a name.  Using the `split` string method on the column `a` to split the URL by `/`.  

Assign your split URL's as a series to `ans3` below.

This series will be a collection of lists:

```python
0       [http:, , dbpedia.org, resource, Deutsche_Euro...
1       [http:, , dbpedia.org, resource, Deutsche_Euro...
2       [http:, , dbpedia.org, resource, Industry_of_M...
3       [http:, , dbpedia.org, resource, Industry_of_M...
4       [http:, , dbpedia.org, resource, Industry_of_M...
         .
         .
         .
```
'''

# YOUR CODE HERE
ans3 = df.loc[df['name'].isnull(), 'a'].str.split('/')
print(ans3)

### Problem 4

#### Extracting the names
'''
**5 Points**

To extract the last element of this list, use the `.apply` method together with an appropriate `lambda` function to create a series based on the last entry of the above list in each row.  Your results should begin with:

```python
0                        Deutsche_EuroShop
1                        Deutsche_EuroShop
2       Industry_of_Machinery_and_Tractors
3       Industry_of_Machinery_and_Tractors
4       Industry_of_Machinery_and_Tractors
                       ...                
```

Save this series to `ans4` below.
'''

# YOUR CODE HERE
ans4 = ans3.apply(lambda x: x[-1])
print(ans4.head())

### Problem 5

#### Filling the Missing Values in `name` 
'''
**5 Points**

The `.fillna` method can accept a series and fill in the missing values based on the matching indices.  


Use the series assigned to `ans4` you created in Problem 4 to fill in the missing values in the `name` column. 

Overwrite the earlier column and create a DataFrame with no missing values in the `name` column and assign this new DataFrame to `ans5` below.
'''

# YOUR CODE HERE
df['name'] = df['name'].fillna(ans4)
ans5 = df
print(ans5['name'].isnull().sum())  # Should print 0

### Problem 6

#### `location` missing values
'''
**5 Points**

Note that the `location` column is still having missing data.  The column is supposed to represent the location of the company as a URL in `dbpedia` or, in some cases, simply the name of the city where the company is located.  


Use the `isnull()` function to count how many missing values are in the `location` columns. Next, use the `value_counts()` function on the `foundation` column.  Assign these counts as a series to `ans6` below.
'''
# YOUR CODE HERE
missing_location_count = df['location'].isnull().sum()
ans6 = df['foundation'].value_counts()
print("Missing values in 'location':", missing_location_count)  

### Problem 7

#### Replace missing `location` with `foundation`
'''
**5 Points**

While not perfect, the values in the `foundation` column could serve as a fill-in for the missing values in `location`.  Replace the missing values in `location` with their corresponding value in `foundation`.  Assign the series with the value filled for `location` to `ans7` below.

**HINT**: Check if the values of `location` is missing using `[df['location'].isnull()]` and use `.fillna()` to fill it with `foundation`
'''

# YOUR CODE HERE
ans7 = df['location'].fillna(df['foundation'])
print(ans7)

### Problem 8

#### Drop rows missing revenue and profit
'''
**5 Points**


Note that the `revenue` and `profit` columns do not have all their values.  


Use the function `dropna()` on `df` to select the non-null entries in the `subset` with columns `revenue` and `profit`.  

Assign your answer as a DataFrame to `ans8` below.
'''

# YOUR CODE HERE
ans8 = df.dropna(subset=['revenue', 'profit'])
print(ans8)

### Problem 9

#### How many rows were lost?
'''
**5 Points**

Compare the shape of the original dataset to your solution in 8.  How many rows were lost dropping the data?  Assign your answer as an integer to `ans9` below.
'''

# YOUR CODE HERE
rows_lost = df.shape[0] - ans8.shape[0]
ans9 = rows_lost
print(ans9)