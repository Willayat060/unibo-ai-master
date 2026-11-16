# A slice returns a copy
# It is a shallow copy: only the outermost level is copied (while the tuple elements are shared).

# But if the slide is complete, i.e. with [::] or equivalent, the implementation CPython returns
# that same outermost tuple (and with the same tuple elements, which are now shared).
# Here the inner tuple elements are shared between S1 and S2 (and S3, apart from the first)

S1 = ((1,2),(3,4),(5,6))
S2 = S1[::]
S3 = S1[1::]

# see on Pythontutor
print(S1 is S2)   # True in CPython: same outermost tuple 
print(S3 is S1)   # False

print(S1[0] is S2[0])   # True: shared inner elements (irrespective of their mutability)

# For lists, being mutable, even complete slices do not reuse the outermost level.
# Again, the inner tuple elements are shared between S1 and S2 (and S3, apart from the first)

S1 = [(1,2),(3,4),(5,6)]
S2 = S1[::]
S3 = S1[1::]

# see on Pythontutor
print(S1 is S2)    # False: a new outermost list
print(S3 is S1)    # False

print(S1[0] is S2[0])   # True: shared inner elements (irrespective of their mutability)
