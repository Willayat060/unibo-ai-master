import numpy as np

a = np.arange(1, 11)

# parentheses around individual comparisons are important
#because of Python's operator precedence. Try without.
mask = (a % 2 == 0) & (a > 4)

# advanced indexing 1: boolean indexing 

print(mask)
print(a[mask])
print(a[(a < 3) | (a > 8)])