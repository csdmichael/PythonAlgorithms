import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
#read in the data
baseball_salaries = pd.read_csv('aiMl/SciPyStats/data/baseball.csv', index_col=0)

#summary statistics
summary = baseball_salaries.describe()
print(summary)

mean = baseball_salaries['salary'].mean()
std = baseball_salaries['salary'].std()

print(f"Uniform Distribution for data: mean = {mean}, std = {std}")

#plot a histogram of the salaries
sampleSize = 1000
U = stats.uniform(loc=baseball_salaries['salary'].min(), 
                  scale=baseball_salaries['salary'].max()-baseball_salaries['salary'].min())
#samples = U.rvs(size=sampleSize) #random variates
samples = baseball_salaries['salary'].sample(sampleSize, replace=True)

mean = samples.mean()
std = samples.std()

print(f"Uniform Distribution for Sample size = {sampleSize}: mean = {mean}, std = {std}")

plt.hist(samples, bins=10, density=True, alpha=0.5, color='g')
plt.title(f'Uniform Distribution of Baseball Salaries, Sample Size = {sampleSize}')
plt.xlabel('Salary')
plt.ylabel('Density')
#plt.show()



