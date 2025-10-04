number = int(input())
speedlimit = 0
national = 20
for i in range(number):
    speed = input()
    if speed == '/':
        print(national)
    else:
        speed = int(speed)
        print(speed)
        if speed >= national:
            national = (speed - speed % 10) + 10

    
    
