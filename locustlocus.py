import math
b = int(input())
locust = []
LCM = []
for i in range(b):
    locust.append(list(map(int, input().split())))
    LCM.append(locust[i][0]+(locust[i][1]*locust[i][2]/math.gcd(locust[i][1],locust[i][2])))
print(int(min(LCM)))


    
