line = list(input())
print(line)
correct = ['U','A','P','C']
for i in range(len(line)):
    if line[i] in correct:
        correct.remove(line[i])
print(correct)
