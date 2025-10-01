a = int(input())
coffees = 0
lecturesawake = a
b = list(input())
print(b)
for i in range(a):
    if (b[i] == '0' and coffees-1>=0):
        coffees -= 1
    elif (b[i] == '0' and coffees==0):
        lecturesawake= lecturesawake - 1
    else:
        coffees += 2-coffees
print(lecturesawake)

        

