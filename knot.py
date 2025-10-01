b = int(input())
lists = []
for i in range(2):
    lists.append(input().split())
for i in range(len(lists[1])):
    if lists[0][i] not in lists[1]:
        print(lists[0][i])
        break




