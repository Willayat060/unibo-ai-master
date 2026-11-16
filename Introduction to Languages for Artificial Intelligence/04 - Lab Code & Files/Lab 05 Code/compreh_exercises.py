
#Given a unary function f and a sequence S, return the list of the application of f to the elements of S

def addone(x):
    return x+1 

S = range(5)
L = [addone(x) for x in S]
print(L)


#Or as a function that receives f as argument:

def apply_f(f, S):
    return [f(x) for x in S]

L = apply_f(addone,S)


#indeed remember that functions are object:

def f(x):
    def g(y):
        return x+y
    return g

myfunction = f(2)	# myfunction is bound to function object g returned by f, remembering x = 2
print(myfunction(4))	# y =4, so the result is 4+2


#--------------------


# Given two sequences S1 and S2 return the list of the elements present in both S1 and S2

S1 = [7, 3, 1, 14, 6, 4, 3]
S2 = [1, 4, 7, 6, 5]

L = [x for x in S1 if x in S2]
print(L)


#--------------------


# pythagorean triples

# we avoid permutation by imposing an order on a,b,c. Here a <= b <= c:

def pythagorean(k):
    return [(a, b, c)
            for a in range(1, k + 1)
            for b in range(a, k + 1)
            for c in range(b, k + 1)
            if a*a + b*b == c*c and a + b + c <= k]

def pythagorean2(k):
    return [(a, b, c)
            for a in range(1, k + 1)
            for b in range(1, k + 1)
            for c in range(1, k + 1)
            if a < b < c		# Here a < b < c explicitly (b<c is implied)
            and a*a + b*b == c*c
            and a + b + c <= k]

# if we allow permutations

def pythagorean3(k):
    return [(a, b, c)
            for a in range(1, k + 1)
            for b in range(1, k + 1)
            for c in range(1, k + 1)
            if a*a + b*b == c*c
            and a + b + c <= k]


print(pythagorean(20))


#--------------------



# permutations

# choose each element in turn as the first element, then find all permutations of the remaining elements.


def erase(e, L):
    V = L[:]		#copy (outermost level)
    V.remove(e)
    return V		# not: return V.remove(e) !

def permutations(L):
    if len(L) <= 1:
        return [L[:]]	#copy (outermost level)

    Res = []

    for e in L:
        rest = erase(e, L)	# with slicing: rest = L[:i] + L[i+1:]

        for p in permutations(rest):
            res([e] + p)

    return res