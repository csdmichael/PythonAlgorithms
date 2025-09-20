import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def column_range(col):
    '''
    This function takes in a pandas series and returns
    the range of the series (max - min) as a float.
    '''
    return col.max() - col.min()


gapminder = px.data.gapminder()
gapminder.info()
print(gapminder.head())

ans5 = gapminder.groupby('continent')[['gdpPercap']].apply(column_range).sort_values(by='gdpPercap', ascending=False)
print(ans5)

ans2 = gapminder.groupby('country')[['gdpPercap']].max().idxmax().values[0]
print(ans2)

#Sorting Results of Multiple Aggregates
ans3a = gapminder.groupby('continent')[['lifeExp']].agg(['mean', 'std', 'median'])
ans3a.columns = [" ".join(c) for c in ans3a.columns.to_flat_index()]
ans3b = ans3a.sort_values(by='lifeExp median', ascending=False)

# Answer check
print(ans3a)
print(ans3b)

ans1 = gapminder.groupby('continent')[['lifeExp']].mean().sort_values('lifeExp', ascending=False)
print(ans1)


#Problem 1
ans1 = gapminder.groupby('year')['lifeExp'].mean()
print(ans1)

#Problem 2
ans2 = gapminder.groupby('continent')['gdpPercap'].mean()
print(ans2)

#Problem 3
ans3 = gapminder.groupby('continent')[['gdpPercap']].agg(['mean', 'median', 'std'])
print(ans3)

#Problem 4
ans4 = gapminder.query('pop > 300_000_000').groupby('pop')[['lifeExp']].mean()
print(ans4)

#Problem 5
continents_to_select = ['Americas', 'Europe']
# Use .isin() to create a boolean mask for the 'continent' column
continent_mask = gapminder['continent'].isin(continents_to_select)

# Filter the DataFrame using the boolean mask and assign to ans5a
ans5a = gapminder[continent_mask]
print(ans5a)

ans5b =  ans5a.groupby(['continent', 'country'])[['lifeExp']].mean()
print(ans5b)

import seaborn as sns

#Problem 6
plt.figure(figsize=(10, 6)) # Set the figure size
sns.barplot(data=ans5b, x='country', y='lifeExp')
plt.title('Life Expectancy by country in Americas and Europe')   
plt.xlabel('Country')
plt.ylabel('Life Expectancy')
plt.xticks(rotation=90) # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping of tick-labels
plt.show()
