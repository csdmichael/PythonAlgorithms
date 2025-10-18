### Getting the Data
'''
Below, we access the data directly using the url and the `read_html` method from `pandas`.  This method reads any table from a web URL as a list of data frames.  The data we are interested in is located in the fifth table on the page, so we index the list of data below.
'''
import pandas as pd
russian_states = pd.read_csv('aiMl/DataCleaning/data/russian_states.csv', index_col = 0)
print(russian_states.head())

### Problem 1

#### Using the `contains` method
'''
**5 Points**

Use the string method `contains` to subset the data based on entries in the `Economic region` column containing `Siberian`.  Assign your response as a DataFrame to `ans1` below.
'''
# YOUR CODE HERE
ans1 = russian_states[russian_states['Economic region'].str.contains('Siberian')]

# Answer check
print(ans1.shape)
ans1.head()

### Problem 2

#### Using the `startswith` method
'''
**5 Points**

Subset the data based on entries in the `Economic region` column that starts with `North.`  Assign your answer as a DataFrame to `ans2` below.
'''
ans2 = russian_states[russian_states['Economic region'].str.startswith('North')]
# Answer check
print(ans2.shape)
ans2.head()

### Problem 3: Using the `upper` method
'''
**5 Points**

Use the `upper` method to create a series where the entries in the `Federal district` column all uppercased.  Assign your response as a Series to `ans3` below.
'''

ans3 = russian_states['Federal district'].str.upper()
# Answer check
print(ans3.head())

### Problem 4

#### Examining the Population
'''
**5 Points**
 

Much like the example in the videos, the `Population[17]` column contains problematic characters that need to be replaced before the column can be converted to a float datatype.  Replace the `\[22\]`, `\[23\]`, and `,` values with empty strings. Finally, convert the `Population[17]` column to `float` datatypes.  

Assign your response as a series to `ans4` below.  
'''

ans4 = russian_states['Population[17]'].str.replace(r'\[22\]', '', regex=True).str.replace(r'\[23\]', '', regex=True).str.replace(',', '').astype(float)
# Answer check
print(ans4.head())