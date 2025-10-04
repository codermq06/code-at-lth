day1 = input().split()
day2 = input().split()
time1 = day1[1].split(":")
time2 = day2[1].split(":")

weekdays = {'Mon' : 0, "Tue" : 1, "Wed":2,"Thu":3,"Fri":4, "Sat":5, "Sun":6}

if time1[0][0] == "0" :
    time1[0] = time1[0][1:]
if time1[1][0] == "0" :
    time1[1] = time1[1][1:]
if time2[0][0] == "0" :
    time2[0] = time2[0][1:]
if time2[1][0] == "0" :
    time2[1] = time2[1][1:]
time1[0], time1[1], time2[0], time2[1] = int(time1[0]), int(time1[1]), int(time2[0]), int(time2[1])
minutes = (time2[1] - time1[1]) % 60
overload = 0
if (time2[1] - time1[1]) < 0:
    overload = 1

hours = (time2[0] - time1[0] - overload) % 24
if (time2[0] - time1[0] - overload) < 0:
    overload = 1
else:
    overload = 0

days = (weekdays[day2[0]]-weekdays[day1[0]] - overload) % 7

def Isplural(numbers):

    if numbers > 1:
        return "s"
    else:
        return ""



if days == 0:
    if hours == 0:
        if minutes == 0:
            print('7 days')
        else:
            print(str(minutes) + ' minute'+ Isplural(minutes))
    elif (minutes == 0):
        print(hours, 'hour' + Isplural(hours))
    else:
        print(hours, 'hour' + Isplural(hours), 'and', minutes, "minute" + Isplural(minutes))
elif (hours == 0):
    if minutes == 0:
        print(days, 'day' + Isplural(days))
    else:
        print(days, 'day' + Isplural(days), 'and', minutes, 'minute' + Isplural(minutes))
elif (minutes == 0):
    print(days, 'day' + Isplural(days),"and" ,hours ,"hour" + Isplural(hours))
else:
    print(days, 'day' + Isplural(days) + ',', hours, 'hour'+ Isplural(hours) + ",", minutes ,"minute" + Isplural(minutes))
