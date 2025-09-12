from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform
# Create a uniform distribution
U = uniform(loc=10, scale=5)  # Uniform distribution between 0 and 1
x = U.pdf([8, 12, 20]) #probability density function
print(x)

U = uniform(loc=2, scale=6)  # Uniform distribution between 2 and 8
m = U.mean() #mean
v = U.var()  #variance
s= U.std()  #standard deviation

print(m, v, s)



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