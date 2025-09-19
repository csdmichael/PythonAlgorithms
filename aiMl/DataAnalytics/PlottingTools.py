import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

gapminder = px.data.gapminder()

print(gapminder.head())
print(gapminder.continent.unique())
print(gapminder.info())

# Create the histogram
ax = gapminder['lifeExp'].hist()

# Set the title
ax.set_title('Histogram of Life Expentancy')

# Save the plot
plt.savefig('aiML/DataAnalytics/images/plot1.png')
plt.show()

# Create the boxplot
sns.boxplot(x='lifeExp', y='continent', data=gapminder)

# Save the plot
plt.savefig('aiML/DataAnalytics/images/plot2.png')

# Show the plot
plt.show()

# Create the barplot
sns.barplot(x='gdpPercap', y='continent', data=gapminder)

# Save the plot
plt.savefig('aiML/DataAnalytics/images/plot3.png')

# Show the plot
plt.show()

# Create the scatterplot
sns.scatterplot(x='gdpPercap', y='lifeExp', data=gapminder)

# Save the plot
plt.savefig('aiML/DataAnalytics/images/plot4.png')

# Show the plot
plt.show()