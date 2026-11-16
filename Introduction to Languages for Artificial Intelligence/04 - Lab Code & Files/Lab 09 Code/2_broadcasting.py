import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

# Practical check:
# 1- Align the shapes from the right, conceptually adding leading 1s to the shorter shape.
# 2- Compare corresponding dimensions. They are compatible if they are equal or at least one is 1.
# 3- Determine the result shape by taking the larger size in each dimension.

print(a + b)  # (2,1) and (1,3)
print(a + 10) # (2,1) and ()
print(a + np.array([[10], [20]])) # (2,1) and (1,2)