from collections import deque
row, column = map(int, input().split())
grid = []
for i in range(row):
    grid.append(list(input()))
cords = deque()
for i in range(row):
    if 'S' in grid[i]:
        cords.append((i,grid[i].index('S')))
completed = set()
while len(cords) != 0:
    a = (cords[0][0],cords[0][1])
    if a[0]+1 < row:
        if (grid[a[0]+1][a[1]] == '#') and ((a[0]+1,a[1]) not in completed):
            cords.append((a[0]+1,a[1]))
            completed.add((a[0]+1,a[1])) 
    if a[0]-1 >= 0:
        if grid[a[0]-1][a[1]] == '#' and (a[0]-1,a[1]) not in completed:
            cords.append((a[0]-1,a[1]))
            completed.add((a[0]-1,a[1])) 
    if a[1]-1 >= 0:
        if grid[a[0]][a[1]-1] == '#' and (a[0],a[1]-1) not in completed:
            cords.append((a[0],a[1]-1))
            completed.add((a[0],a[1]-1)) 
    if a[1]+1 < column:
        if grid[a[0]][a[1]+1] == '#' and (a[0],a[1]+1) not in completed:
            cords.append((a[0],a[1]+1))     
            completed.add((a[0],a[1]+1)) 
    completed.add(a)
    cords.popleft()
print(len(completed))

        
    
        
            
        



         
    
    
    