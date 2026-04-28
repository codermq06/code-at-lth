a, b = map(int, input().split())
num1 = 0
num2 = 0
for val in map(int, input().split()):
    num1+=val
for val in map(int, input().split()):
    num2+=val
if num1 > num2:
    print("Button 1")
elif num2 > num1:
    print("Button 2")
else:
    print("Oh no")
