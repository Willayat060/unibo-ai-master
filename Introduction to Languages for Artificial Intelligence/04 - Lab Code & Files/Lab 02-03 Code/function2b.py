# Similar example to function2.py

# In this variant, the frame for cylinder_vol has no local binding for r. 
# But the global binding is accessible from within the function. 

r = 100

def cylinder_vol(h):
    pi = 3.1415
    return pi * r**2 * h

print(cylinder_vol(3))


# Frame for cylinder_vol(3):
#     h  : 3
#     pi : 3.1415
# 
# Global frame:
#     r : 100


