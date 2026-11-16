# basic example

temperature = 35

print("Using separate if statements:")

if temperature > 20:
    print("It is warm")
if temperature > 30:
    print("It is hot")
if temperature > 40:
    print("It is extremely hot")

print("Using if / elif / else:")

if temperature > 40:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature > 20:
    print("It is warm")
else:
    print("It is cold")


# more examples of comparisons

x = 10
name = "Alice"
age = 20
has_license = True

# Comparisons
print(x == 10)
print(x != 5)
print(x > 5)
print(x >= 10)
print(x < 20)
print(x <= 10)

# Combining conditions
print(x > 0 and x < 20)
print(x < 0 or x > 5)
print(not x == 5)

# Chained comparisons
print(0 < x < 20)
print(5 <= x <= 10)

# String membership
print("a" in name)
print("z" not in name)

# String comparisons
print(name == "Alice")
print(name != "Bob")
print(name[0] == "A")
print(name[-1] == "e")

# Boolean variables
print(has_license)
print(not has_license)

# Combining different conditions
print(age >= 18 and has_license)
print(age < 18 or not has_license)

# Conditions in if statements
if age >= 18:
    print("Adult")

if age >= 18 and has_license:
    print("Adult with a driving license")

if name == "Alice" or name == "Bob":
    print("Recognized name")

if 0 < x <= 10:
    print("x is between 0 and 10")


### Truthy and Falsy values

### Truthy and Falsy describe how non-Boolean values are treated in a Boolean context: truthy values are treated as True, while falsy values are treated as False. This allows Boolean operations and conditions to be consistently defined for any object, without requiring it to be an actual Boolean value.

# Falsy values

if not None:
    print("None is falsy")

if not 0:
    print("Integer 0 is falsy")

if not 0.0:
    print("Float 0.0 is falsy")

if not "":
    print("An empty string is falsy")


# Truthy values

if 1:
    print("Integer 1 is truthy")

if -5:
    print("A negative nonzero integer is truthy")

if 0.1:
    print("A nonzero float is truthy")

if name:
    print("A non-empty string is truthy")
# If name is either a string or None, this excludes:
# name == ""
# name is None

if "False":
    print("The string 'False' is truthy")

if "0":
    print("The string '0' is truthy")


# Indeed, and/or do not necessarily return Boolean values:  
# They return one of their operands and use short-circuit (lazy) evaluation. 

# Evaluate A first.
#
# A and B:
#    value of A is falsy : return the value of A; B is not evaluated
#    value of A is truthy : evaluate B and return its value
#
# A or B:
#    value of A is truthy : return the value of A; B is not evaluated
#    value of A is falsy  : evaluate B and return its value
#
#
# examples:


# AND: if the first operand is falsy, return it

print(0 and 10)          # 0: the value of A is 0
print("" and "hello")    # "": the value of A is ""

# Otherwise, evaluate and return the second operand

print(5 and 10)          # 10: the value of B is 10


# OR: if the first operand is truthy, return it

print(5 or 10)           # 5: the value of A is 5
print("hello" or "bye")  # "hello": the value of A is "hello"

# Otherwise, evaluate and return the second operand

print(0 or 10)           # 10: the value of B is 10


# Short-circuiting can avoid invalid operations

x = 0
print(x and 10 / x)      # 0

x = 10
print(x or 10 / 0)       # 10


# Observe how this implies that they return Boolean values when A and B are Booleans, as expected. 

print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False