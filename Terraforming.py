a = int(input())
temp = 0
oxy = 0
oce = 0
for i in range(a):
    word = str(input())
    if word[1] == "c":
        oce += int(word[-1])
    elif word[1] == "x":
        oxy += int(word[-1])
    else:
        temp += int(word[-1])
if (oxy > 13 and oce > 8 and temp > 13):
    print("liveable")
else:
    print("unliveable")

