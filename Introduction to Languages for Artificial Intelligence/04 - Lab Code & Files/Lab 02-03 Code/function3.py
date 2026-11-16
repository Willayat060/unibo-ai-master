# The interesting difference from the previous examples is that here
# the name r in the two function-call frames is initially bound to the
# same object (an int with value 2).
#
# When cylinder_vol(2, 3) is called, its parameter r is bound to the
# object resulting from evaluating the argument 2.
#
# Later, when area_circle(r) is called, the argument r is evaluated
# in cylinder_vol's frame, and the resulting object is bound to the
# parameter r in area_circle's new frame.
#
# Thus, the two frames contain separate bindings for the name r,
# but those bindings refer to the same object.

def area_circle(r):
    print(f"area_circle: r={r}, id(r)={id(r)}")
    pi = 3.1415
    return pi * r**2

def cylinder_vol(r, h):
    print(f"cylinder_vol: r={r}, id(r)={id(r)}")
    return area_circle(r) * h

print(cylinder_vol(2, 3))


# Contrast this with the following variant, which adds r = 10
# inside area_circle.
#
# When area_circle is called, its parameter r is initially bound to
# the object passed as the argument. Then r = 10 rebinds that local
# name to another object.
#
# This rebinding affects only r in the frame for area_circle.
# It does not change the binding of r in the frame for cylinder_vol.
#
# def area_circle(r):
#     r = 10
#     pi = 3.1415
#     return pi * r**2