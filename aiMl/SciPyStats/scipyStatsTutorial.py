from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform
# Create a uniform distribution
U = uniform(loc=10, scale=5)  # Uniform distribution between 0 and 1
x = U.pdf([8, 12, 20]) #probability density function
print(x)

upoints = np.linspace(7, 18, 200) # 200 points between 7 and 18
ppoints = U.pdf(upoints)
plt.plot(upoints, ppoints)
plt.title('Uniform Distribution')
plt.show()