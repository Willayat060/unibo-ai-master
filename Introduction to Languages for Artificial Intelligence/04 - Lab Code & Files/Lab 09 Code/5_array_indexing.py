import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# advanced indexing 2: array indexing (using arrays or lists) 
# these all use advanced indexing: copies!

print("Original array:\n", a)
print("a.shape =", a.shape)

print("\n--- Selecting rows ---")
print("a[[0, 2]] =\n", a[[0, 2]])         # Select rows 0 and 2.
print("a[[2, 0, 2]] =\n", a[[2, 0, 2]])   # Select rows in the given order, repeating row 2.
print("a[[-1, 0]] =\n", a[[-1, 0]])       # Select the last row and then the first row.

print("\n--- Selecting individual elements by coordinates ---")
print("a[[0, 2], [1, 0]] =", a[[0, 2], [1, 0]])  # Select elements at coordinates (0,1) and (2,0).
print("a[[0, 1, 2], [2, 0, 1]] =", a[[0, 1, 2], [2, 0, 1]]) # Select elements at (0,2), (1,0), and (2,1).
print("a[[1, 1, 2], [0, 2, 2]] =", a[[1, 1, 2], [0, 2, 2]]) # Select elements at (1,0), (1,2), and (2,2).

print("\n--- Combining slicing and advanced indexing ---")
print(a[:, [2, 0]])  # Select all rows, taking columns 2 and 0.
print(a[[2, 0], :2]) # Select rows 2 and 0, taking their first two columns.
print(a[1:, [0, 2]]) # Select rows 1 onward, taking columns 0 and 2.

print("\n--- Multidimensional integer indices ---")
print(a[np.array([[0, 1], [2, 0]])])   # Select rows using a 2D index array, producing a 3D result.

print("\n--- View or copy? ---")
b = a[[0, 2]]
print(np.shares_memory(a, b))