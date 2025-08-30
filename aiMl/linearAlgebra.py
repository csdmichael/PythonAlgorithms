import numpy as np

def vector_addition(v1, v2):
    return np.add(v1, v2)

def vector_subtraction(v1, v2):
    return np.subtract(v1, v2)

def scalar_multiplication(v, scalar):
    return np.multiply(v, scalar)

def dot_product(v1, v2):
    return np.dot(v1, v2)

def cross_product(v1, v2):
    return np.cross(v1, v2)

# Example usage
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
scalar = 3

#v1 =  np.array([[2,3,1],[4,0,5]])
#v2 =  np.array([[1,4],[2,3],[0,6]])

print("Addition:", vector_addition(v1, v2))
print("Subtraction:", vector_subtraction(v1, v2))
print("Scalar Multiplication:", scalar_multiplication(v1, scalar))
print("Dot Product:", dot_product(v1, v2))
print("Cross Product:", cross_product(v1, v2))
