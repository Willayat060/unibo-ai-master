import numpy as np
       
# We want to exchange adjacent columns: column 0 with 1, and column 2 with 3, etc.

def exchangecolumns(a):
    if a.shape[1]%2 != 0: # must be even
        return None
    # we copy a as b
    b = a.copy()
    # every even column of a is repaced by the next from copy b
    # so there is no potential side-effect.
    a[:,::2],a[:,1::2] = b[:,1::2],b[:,::2]
    return a

def exchangecolumns2(a):
    if a.shape[1]%2 != 0: # must be even
        return None
    # b = a.copy() # WITHOUT copy()
    # this does not work as expected: the RHS is evaluated first,
    # then the assignments are performed in order. 
    # So the first assignment a[:,::2]= a[:,1::2] causes the
    # second to perform the wrong update: a was already updated
    # and since a[:,::2] is a VIEW, its value has changed already.
    a[:,::2],a[:,1::2] = a[:,1::2],a[:,::2]
    return a


a = np.arange(6).reshape(3, 2)

print("\n--- Example 1: 3 rows, 2 columns ---")
print("Original array:")
print(a)
print("exchangecolumns (with copy):")
print(exchangecolumns(a.copy()))
print("exchangecolumns2 (without copy):")
print(exchangecolumns2(a.copy()))

a = np.arange(20).reshape(5, 4)

print("\n--- Example 2: 5 rows, 4 columns ---")
print("Original array:")
print(a)
print("exchangecolumns (with copy):")
print(exchangecolumns(a.copy()))
print("exchangecolumns2 (without copy):")
print(exchangecolumns2(a.copy()))
