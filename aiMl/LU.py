# LU decomposition
from numpy import array
from scipy.linalg import lu
# define a square matrix
#A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A = array([[2,1], [8,7]])
print(A)
# LU decomposition
L, U = lu(A)
print(L)
print(U)
# reconstruct
B = L.dot(U)
print(B)