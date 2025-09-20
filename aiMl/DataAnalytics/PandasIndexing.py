import pandas as pd
import plotly.express as px

gapminder = px.data.gapminder()
gapminder.info()
print(gapminder.head())

# What fraction of world GDP did each country generate each year?
#df = gapminder.groupby(['year', 'country'])[['gdp']].sum()
#print(df.head())

