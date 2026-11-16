import numpy as np

a = np.arange(6).reshape(2, 3)
v = np.array([1, 2, 3])

print(a)                         # Display the original 2D array.
print(a.T)                       # Transpose the array by exchanging its axes.
print(a.shape, a.T.shape)        # Compare the shapes before and after transposition.

print(v.shape, v.T.shape)        # Show that transposing a 1D array does not change its shape.
print(v.reshape(1, 3))           # Convert the 1D array into a 2D row vector.
print(v.reshape(1, 3).T)         # Transpose the row vector into a column vector.
print(v.reshape(1, 3).T.shape)   # Display the column vector's shape.

print(a.reshape(3, 2))           # Reshape the original array without changing element order.
print(a.T.reshape(3, 2))         # Reshape the transposed array and compare the values.