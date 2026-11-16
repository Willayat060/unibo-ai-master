X=1
def nested_class_def():
    X=2       # it shadows the global X
    print(X)  # second output: 2 
    
    class C:
        X=3   # class attribute
        print(X) # third output: 3 (a class body has its own scope)
        
        def m1(self):
            print(X)         # fourth output: 2, not 3
            # A class body has its own scope, but that scope is not an "enclosing scope" 
            # (non-local scope) for methods defined within the class. See last slides.
            # Now change it to print(C.X), which prints 3: the value of the class attribute
            
            print(self.X)    # fifth output: 3 (not a LEGB lookup of name X, but simply an attribute)
    
    I = C()    # causes the third output: 3
    I.m1()
    
print(X)                     # first output: the global 1
nested_class_def()           
