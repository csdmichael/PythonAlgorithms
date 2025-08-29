import matplotlib.pyplot as plt

import numpy as np



# Define vectors

v1 = np.array([3, 4, 5])

v2 = np.array([2, 1, 6])



# Vector operations

v_add = v1 + v2

v_sub = v1 - v2

dot_product = np.dot(v1, v2)

cross_product = np.cross(v1, v2)



# Plot setup

plt.figure(figsize=(8, 8))



# Original vectors

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1 = [2, 3]')

plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2 = [4, 1]')



# Vector addition (v1 + v2)

plt.quiver(0, 0, v_add[0], v_add[1], angles='xy', scale_units='xy', scale=1, color='g', alpha=0.6, label='v1 + v2')



# Vector subtraction (v1 - v2)

plt.quiver(0, 0, v_sub[0], v_sub[1], angles='xy', scale_units='xy', scale=1, color='m', alpha=0.6, label='v1 - v2')



# Axes settings

plt.xlim(-3, 8)

plt.ylim(-3, 8)

plt.grid()

plt.axhline(0, color='black', linewidth=0.5)

plt.axvline(0, color='black', linewidth=0.5)

plt.gca().set_aspect('equal', adjustable='box')

plt.legend()

plt.title('2D Vector Operations')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')



# Print dot and cross product

print(f"Dot Product (v1 • v2): {dot_product}")

print(f"Cross Product (v1 x v2): {cross_product}")



# Show plot

plt.show()