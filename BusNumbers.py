import math
b = int(math.sqrt(int(input())))
numberlist = []
finalnumber = []
for i in range(1,b):
    for y in range(i,b):
        a = i**3 + y**3
        if a not in numberlist:
            numberlist.append(a)
        else:
            finalnumber.append(a)
print(finalnumber)
t = b**3
set = "none"
print(t)
for i in finalnumber:
    if t < i:
        break
    else:
        set = i
print(set)
    
