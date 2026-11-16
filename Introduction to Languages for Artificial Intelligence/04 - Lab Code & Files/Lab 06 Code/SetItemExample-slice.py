#see SetItemExample first

class SetItEx:
    def __init__(self):
        self.V=[10,20,30,40]
        
    def __len__(self):
        return len(self.V)
    
    def __getitem__(self,key):
        if isinstance(key, slice):
            # a slice object (with attributes start,stop,step)
            return self.V[key.start:key.stop:key.step]
        else:
            # a plain index
            return self.V[key]
        
    def __setitem__(self, key, val):
        if key>len(self.V):
            return None
        if key==len(self.V):
            self.V.append(val)
        else:
            self.V[key]=val

S=SetItEx()
print(len(S))  # 4  Calls __len__
S[0]=10        # Calls __setitem__
print(len(S))  # 4  
print(S[0])    # 10 Calls __getitem__