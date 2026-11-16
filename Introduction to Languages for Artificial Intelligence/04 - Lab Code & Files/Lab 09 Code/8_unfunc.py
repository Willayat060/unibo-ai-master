import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20])

print("a =", a)
print("b =", b)

print("\n--- Elementwise operations ---")
print("np.add(a, 5) =", np.add(a, 5))
print("np.multiply(a, 2) =", np.multiply(a, 2))
print("np.square(a) =", np.square(a))
print("np.sqrt(a) =", np.sqrt(a))

# reduce() — combines elements into a single result (by default for a 1D array).
# accumulate() — retains the intermediate results of successive combinations.
# outer() — applies the operation to every possible pair of elements from the two input arrays.

print("\n--- Reductions ---")
print("np.add.reduce(a) =", np.add.reduce(a))
print("np.multiply.reduce(a) =", np.multiply.reduce(a))
print("np.maximum.reduce(a) =", np.maximum.reduce(a))

print("\n--- Cumulative operations ---")
print("np.add.accumulate(a) =", np.add.accumulate(a))
print("np.multiply.accumulate(a) =", np.multiply.accumulate(a))

print("\n--- Outer operations ---")
print("np.add.outer(a, b) =\n", np.add.outer(a, b))
print("np.multiply.outer(a, b) =\n", np.multiply.outer(a, b))

print("\n--- Result shapes ---")
print("np.add(a, 5).shape =", np.add(a, 5).shape)
print("np.add.reduce(a).shape =", np.add.reduce(a).shape)
print("np.add.accumulate(a).shape =", np.add.accumulate(a).shape)
print("np.add.outer(a, b).shape =", np.add.outer(a, b).shape)