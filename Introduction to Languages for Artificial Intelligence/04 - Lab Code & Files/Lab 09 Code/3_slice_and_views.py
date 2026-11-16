import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = a[1:4]
c = a[[1, 2, 3]]

b[0] = 99
c[1] = 88

print(a)
print(b)
print(c)

print(np.is_base(a, b))
print(np.shares_memory(a, c))