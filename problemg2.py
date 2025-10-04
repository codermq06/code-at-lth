kids, fs, gv = map(int,input().split())
graphs = []


for i in range(fs):
    a,b = map(int,input().split())
    check = False
    for i in range(len(graphs)):
        if a in graphs[i] and b not in graphs[i]:
            graphs[i].append(b)
            check = True
            break
        elif b in graphs[i] and a not in graphs[i]:
            graphs[i].append(a)
            check = True
            break
        elif b in graphs[i] and a in graphs[i]:
            check = True
            break

    if not check:
        graphs.append([a,b])
#new_set = []
#for graph in graphs:
#    ls = graphs
 #   for graph2 in graphs:
  #      if ls != graph2 :
   #         if len(set(ls) & set(graph2)) != len(ls) + len(graph2):
   #             new_set.append(list(set(ls) & set(graph2)))
            
#print(new_set)



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
