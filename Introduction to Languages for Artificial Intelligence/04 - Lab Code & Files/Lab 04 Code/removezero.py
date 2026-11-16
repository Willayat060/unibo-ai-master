def remove_zero(L):
    i=0
    while i<len(L):
        if L[i]==0:
            del L[i]
        else:
            i=i+1
    return L


S=[1,2,3,0,4,5,6,0]
remove_zero(S)
print(S)

# A wrong attempt:

def remove_zero_for(L):
  #WRONG! It will result in "list index out of range"
    for i in range(len(L)):
        if L[i]==0:
            del L[i]
    return L
    
''' Remember that the expression after "in" is evaluated only once (the object "frozen"): here we obtain range(8). 
Since a range is immutable, subsequent changes to L do not change the range value, hence the error.''' 

''' Note how this differs from writing "for el in L:" when L is a list, because lists are mutable. However, as shown 
below in the last example, we can't use this for deletion. ''' 

''' There's another problem as well in the code above: deletion shifts subsequent elements to the left, 
which can cause zeros in the list to be skipped. So it would not work anyways.
Modifying the structure of a list while iterating forward over its original indices is often problematic.''' 

# Another wrong attempt:

def remove_zero_nonselection(L):
  #WRONG! It does not modify the list, because "del" is not called on a selection
    for e in L:
        if e==0:
            del e	# it simply deletes the binding of the name e (which is then re-bound at the next iteration)