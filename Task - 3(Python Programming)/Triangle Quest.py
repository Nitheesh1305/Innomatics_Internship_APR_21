for i in range(1,int(input())): 
    print(int((i*(pow(10, i) - 1)) / 9 )) 

#Another Solution 
for i in range(1,input()): 
    print(int(str(i)*i))