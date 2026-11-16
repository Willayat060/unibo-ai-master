# this a generator expression, not a tuple. You cannot use selection

G=(i*2 for i in range(4))

print(G)

print(next(G))
print(next(G))
print(next(G))
print(next(G))
####print(next(G))


#--------------------


# You do not get 10. G is now a generator object.

def f():
    yield 10

G = f()

print(next(G))


"""
The call to the function will not execute the body. 
The body is executed when I call next on F, up to the FIRST yield 
The frame for the function call is NOT destroyed, just suspend the execution
When next will be called again, the execution will be RESUME

When the execution reaches the end (return None or implicitly), 
the StopIteration exception will be raised 
"""


#--------------------


def f():
    yield 1
    yield 2
    yield 3

g = f()

print(next(g))   # 1
print(next(g))   # 2
print(next(g))   # 3



#--------------------

def f(n):
    i = 0
    while i < n:
        yield i
        i+=1


F=f(9)

print(next(F))
print(next(F))
print(next(F))