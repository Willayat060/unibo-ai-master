D = {"a": 1, "b": 2}
k = D.keys() #view object on the keys

D["c"] = 3

print(k) # dict_keys(['a', 'b', 'c'])

# Although we created k before adding "c",
# k reflects the change.
# The view remains connected to the dictionary.
# They are a "view" on the data.

# compare the above with this (see also pythontutor):

D = {"a": 1, "b": 2}
L = list(D.keys()) # a **list** from the view

D["c"] = 3

print(L) # ['a', 'b'] - L has no key 'c'


# But thet are NOT sequences in the Python sense we studied:
# although for,in,len(),etc are defined (and they are iterable),
# for example selection [] is not defined. For instance, this
# gives a TypeError saying the object is not subscriptable, 
# i.e. we can't use indexes: 
# print(D.keys()[1]) 