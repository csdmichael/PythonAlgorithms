import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nyc_salary_data = pd.read_csv('aiMl/outliers/data/nyc_salaries.csv')

info = nyc_salary_data.info()
print(info)

head = nyc_salary_data.head()
print(head)

nyc_salary_data['base_salary'].hist()
plt.show()

first_quartile = ''
third_quartile = ''

###BEGIN SOLUTION
first_quartile = nyc_salary_data['base_salary'].quantile(.25)
third_quartile = nyc_salary_data['base_salary'].quantile(.75)

iqr = third_quartile - first_quartile

lower = ''
upper = ''

###BEGIN SOLUTION
first_quartile = nyc_salary_data['base_salary'].quantile(.25)
third_quartile = nyc_salary_data['base_salary'].quantile(.75)
iqr = nyc_salary_data['base_salary'].quantile(.75) - nyc_salary_data['base_salary'].quantile(.25)
lower = first_quartile - 1.5*iqr
upper = third_quartile + 1.5*iqr

salaries_no_outlier = ''

###BEGIN SOLUTION
first_quartile = nyc_salary_data['base_salary'].quantile(.25)
third_quartile = nyc_salary_data['base_salary'].quantile(.75)
iqr = nyc_salary_data['base_salary'].quantile(.75) - nyc_salary_data['base_salary'].quantile(.25)
lower = first_quartile - 1.5*iqr
upper = third_quartile + 1.5*iqr
salaries_no_outlier = nyc_salary_data.loc[(nyc_salary_data['base_salary']>lower) & (nyc_salary_data['base_salary']<upper)]
print(salaries_no_outlier)

mean = np.mean(nyc_salary_data['base_salary'])
mean_no_outlier = np.mean(salaries_no_outlier['base_salary'])
print("Mean with outliers: ", mean)
print("Mean without outliers: ", mean_no_outlier)

len_original = len(nyc_salary_data)
len_no_outlier = len(salaries_no_outlier)
print("Length of original data: ", len_original)
print("Length of data without outliers: ", len_no_outlier)

salaries_no_outlier['base_salary'].hist()
plt.show()