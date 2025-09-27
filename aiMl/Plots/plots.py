import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

pio.renderers.default = "notebook"
#pio.renderers.default = "vscode"

gapminder = px.data.gapminder()
print(gapminder.head())

fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", color="country", size='pop', hover_name='country',
                 log_x=True, size_max=60, animation_frame="year", animation_group="country",
                 title="Gapminder: GDP per Capita vs Life Expectancy")
fig.show(renderer="svg")

fig2 = px.box(gapminder, x="continent", y="gdpPercap", color="continent",
              title="Gapminder: Life Expectancy by Continent")