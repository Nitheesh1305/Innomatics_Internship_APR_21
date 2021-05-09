N = int(input())

for i in range(N):
    line = input()
    while (' && ' in line) or (' || ' in line):
        line = line.replace(' && ', ' and ')
        line = line.replace(' || ', ' or ')
        
    print(line)    