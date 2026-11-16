# O(n), max n/2 comparisons,
# returns false as soon as test fails 
def is_palindrome(S):
    for i in range(len(S) // 2):
        if S[i] != S[-i - 1]:
            return False

    return True

# O(n), but creates reversed string
def is_palindrome_slice(S):
    return S == S[::-1]

# O(n^2) in space/time, with n/2+1 frames on the stack
def is_palindrome_rec(S):
    
    #base case
    if len(S) <= 1:
        return True
    
    #test
    if S[0] != S[-1]:
        return False

    return is_palindrome_rec(S[1:-1])
    # note the slice! this is quadratic: (n-2)+(n-4)+(n-6)+...
    
    
# Using indexes to avoid the slice, we either assume the function
# will be called with the right arguments (index 0 and index len(S)-1)
# or we could even write a nested function to hide this detail to the caller
def is_palindrome_rec_indexes(S):

    #inner function definition (recall that a def is just a command, so we can use it here)
    def inner(left, right):
        if right <= left:
            return True

        if S[left] != S[right]:
            return False

        return inner(left+1, right-1)

    #call to the inner function (after its defintion), making sure the arguments are correct
    return inner(0, len(S)-1)

    
print(is_palindrome("ABBA"))    

# do these work with other sequences?