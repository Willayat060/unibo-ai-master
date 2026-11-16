L=[11,4,8,5]
V=L
L.sort()
print(L)
print(V is L)
print(id(V),id(L))

L=[11,4,8,5]
M=sorted(L)
print(M is L)
