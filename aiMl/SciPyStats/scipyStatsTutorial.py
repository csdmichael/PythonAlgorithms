from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform
# Create a uniform distribution
U = uniform(loc=10, scale=5)  # Uniform distribution between 0 and 1
x = U.pdf([8, 12, 20]) #probability density function
print(x)

p_less_than_12 = U.cdf(12)
cdf_11 = U.cdf(11)
cdf_13 = U.cdf(13)
p_between_11_and_13 = cdf_13 - cdf_11
p_greater_than_12 = 1 - p_less_than_12
print(p_less_than_12, p_between_11_and_13, p_greater_than_12)

U = uniform(loc=2, scale=6)  # Uniform distribution between 2 and 8
m = U.mean() #mean
v = U.var()  #variance
s= U.std()  #standard deviation

print(m, v, s)

y = U.cdf(x<5)
print('y', y) #cumulative distribution function

#Sampling
samples = U.rvs(size=3) #random variates
print("Samples", samples)

samples = U.rvs(size=20000) #random variates
plt.hist(samples, bins=10, density=True, alpha=0.5, color='g')
plt.show()

upoints = np.linspace(7, 18, 200) # 200 points between 7 and 18
ppoints = U.pdf(upoints)
plt.plot(upoints, ppoints)
plt.title('Uniform Distribution')
plt.show()