from random import randint

def howmanybefore(x):
    if x<0 or x>99:
        return -1
    
    extract=randint(0,99)
    howmany=1
    
    while extract!=x:
        extract=randint(0,99)
        howmany=howmany+1
        
    return howmany
    
    
# The function above uses a condition-controlled loop, adopting the canonical pattern for these examples:
# "Repeat the body while a condition remains true".
#
# Another patter is to perform the test inside the body of each iteration, exiting the while-loop if it is met. 
#
def alternativeExtractionsCount(x):
    if x<0 or x>99:
        return -1

    count = 0

    while True:
        n = randint(0, 99)
        count = count + 1
        if n == x:
            break		# we immediately terminate the current iteration and the loop (this works with for-loops too)

    return count