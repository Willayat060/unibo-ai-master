s = "Hello World"
s = s.lower()

counts = {}

for l in s:
    if l not in counts: #always check!
        counts[l] = 1
    else:
        counts[l] += 1

print(counts)


# or by using the method get(key,default):
# for l in s:
#    counts[l] = counts.get(l, 0) + 1