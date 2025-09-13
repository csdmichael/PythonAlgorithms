import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gap_df = pd.read_csv('aiMl/multiVariatePlots/data/gapminder.csv')
d= gap_df.describe()
print(d)
hist_columns = ['lifeExp', 'pop', 'gdpPercap']
'''
plt.hist(gap_df['lifeExp'])
plt.title('Life Expectancy Distribution')
plt.xlabel('Life Expectancy')
plt.show()

plt.grid()
plt.title('Histogram of  GDP per capita')
plt.xlabel('GDP Per Capita')
plt.hist(gap_df['gdpPercap'], bins=50, edgecolor='black', alpha=0.5, color='lightblue')
'''
plt.scatter(x=gap_df['gdpPercap'], y=gap_df['lifeExp'],c='lightblue', edgecolor='black')
plt.title('GDP vs. Life Expectancy')
plt.xlabel('GDP Per Capita')
plt.ylabel('Life Expectancy (years)')

#plt.savefig('images/life_exp_hist.png')
plt.show()