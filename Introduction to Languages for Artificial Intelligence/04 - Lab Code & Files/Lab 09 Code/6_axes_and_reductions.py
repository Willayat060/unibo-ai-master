import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Original array:\n", a)
print("a.shape =", a.shape)

print("\n--- Basic reductions ---")
print("np.sum(a) =", np.sum(a))
print("np.sum(a, axis=0) =", np.sum(a, axis=0))
print("np.sum(a, axis=1) =", np.sum(a, axis=1))

print("\n--- Result shapes ---")
print("np.sum(a, axis=0).shape =", np.sum(a, axis=0).shape)
print("np.sum(a, axis=1).shape =", np.sum(a, axis=1).shape)

print("\n--- Keeping dimensions ---")
print("np.sum(a, axis=0, keepdims=True) =\n",
      np.sum(a, axis=0, keepdims=True))

print("np.sum(a, axis=1, keepdims=True) =\n",
      np.sum(a, axis=1, keepdims=True))

print("\n--- Other reductions ---")
print("np.mean(a, axis=0) =", np.mean(a, axis=0))
print("np.max(a, axis=1) =", np.max(a, axis=1))

print("\n--- Ufunc reduction ---")
print("np.add.reduce(a, axis=0) =", np.add.reduce(a, axis=0))