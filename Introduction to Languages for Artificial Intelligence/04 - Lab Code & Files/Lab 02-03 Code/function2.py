# Execute this on Python Tutor and observe the distinct frames.

# A frame holds bindings of names during execution.
# Each function call creates a new frame.
#
# A scope is a region of the program in which particular name bindings
# are directly accessible.
#
# So:
# function body : defines a local scope
# function call : creates a local frame
#
# Names assigned inside a def are local to that function
# (unless declared global or nonlocal explicitly in the code).
# They are not directly accessible from outside that function,
# although nested functions can access them through an enclosing scope.
# Local bindings do not clash with bindings for the same name in other scopes.
#
# When Python evaluates a name, it searches for a binding of that name
# according to the LEGB order of scopes:
#
# Local -> Enclosing -> Global -> Built-in
#
# Here Enclosing refers to the local scope of an outer function
# within which the current function was defined:
#
# def outer():
#     def inner():
#         ...


r = 100
print(f"global: r={r}, id(r)={id(r)}")

def cylinder_vol(r, h):
    pi = 3.1415
    print(f"cylinder_vol: r={r}, id(r)={id(r)}")
    return pi * r**2 * h

print(cylinder_vol(2, 3))


# Global frame:
#     r : 100
#     cylinder_vol : function object
#
# Frame for cylinder_vol(2, 3):
#     r  : 2
#     h  : 3
#     pi : 3.1415
#
# There is a global binding r -> 100 and, during this function call,
# a separate local binding r -> 2. Rebinding one does not change the other.