# An assignment to a name anywhere in a function makes that name local
# to the function (unless explicitly declared global or nonlocal).
#
# That is, Python determines local names from the whole function body,
# not line by line.
#

x = 5

def f():
    v = x
    y = 100
    x = 1	# !!

f()


# This raises UnboundLocalError.
#
# Because x = 1 occurs in f, Python treats x as a local name throughout f.
# Namely, x is already classified as a local name when the function begins
# executing, but its local binding is not established until x = 1 executes.
#
# Therefore, when v = x is executed, Python looks for x in the local frame.
# Since no local binding for x has yet been established, an
# UnboundLocalError is raised.

# Consider now these two modifications, and understand the difference:
# modification 1: remove x=1
# modification 2: move x=1 to the beginning of the function's body 
# modification 3: declare the function as f(x)
