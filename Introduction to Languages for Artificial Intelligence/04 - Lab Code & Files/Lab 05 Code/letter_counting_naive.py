# naive approach without dictionary: we obtain two lists, and it is 
# our responsibility to maintain their coherence if we update them later

s = "Hello World"
s = s.lower() #we don't want to distinguish a/A

letters = []
count = []
for l in s:

    if l not in letters:
        letters.append(l)
        count.append(1)
    
    #l is in letters
    else: 
        count[letters.index(l)] += 1 

print(letters, count)


# here += is better than count[...] = count[...]+1 ! the index is computed once (see slides)