# without a function:

R = float(input("give R\n"))
H = float(input("give H\n"))
volume = (3.1415*R**2)*H
print(volume)

# with a function:

def cylinder_vol(r,h):
    pi=3.1415
    return (pi*r**2)*h

print(cylinder_vol(R,H))

# Note: functions are first-class citizens. Analyze this file on pythontutor to see 
# how the the binding of functions is represented.
print(cylinder_vol)
print(type(cylinder_vol))