#Question 7 - Print Function 

#Read an integer,n,
#Without using any string methods, try to print the following: 123.....n

n=int(input('Entewr a integer:'))

for i in range(1,n+1):
    print(i,end='')
