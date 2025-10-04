kids, fs, gv = map(int,input().split())
graphs = []


for i in range(fs):
    a,b = map(int,input().split())
    check = False
    for i in range(len(graphs)):
        if a in graphs[i] and b not in graphs[i]:
            graphs[i].append(b)
            check = True
        elif b in graphs[i] and a not in graphs[i]:
            graphs[i].append(a)
            check = True
        elif b in graphs[i] and a in graphs[i]:
            check = True

            
    if not check:
        graphs.append([a,b])

possible = True
sum = 0
for graph in graphs:
    sum += len(graph)
    if len(graph) < gv:
        print("impossible")
        possible = False
        break
if sum < kids and gv > 1 and possible == True:
    possible = False
    print('impossible')
elif sum <= kids and gv == 1:
    for i in range(1,kids + 1):
        print(1)
    possible = False

print(graphs)
if possible:
    for i in range(1, kids+1):
        for graph in graphs:
            if i in graph:
                print(((graph.index(i) % gv)+1))

    

        

    
            
        

