class SetItEx:
    def __init__(self):
        self.V=[1]
        self.ll=0
        
    #We define the bahavior of len().
    #As an example, we define the length as len(V)+ll.
    def __len__(self):
        return len(self.V)+self.ll
    
    #For retrieving an element of V, given an index.
    #This can throw a IndexError: list index out of range.
    def __getitem__(self,key):
        return self.V[key]
    
    #For updating V.
    def __setitem__(self, key, val):
        if key>len(self.V):
            return None
        if key==len(self.V):
            self.V.append(val)
        else:
            self.V[key]=val

S=SetItEx()
print(len(S))  # 0  Calls __len__
S[0]=10        # Calls __setitem__
print(len(S))  # 1  Calls __len__
print(S[0])    # 10 Calls __getitem__