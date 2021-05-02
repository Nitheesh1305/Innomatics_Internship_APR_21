# Question 8 - No Idea !

  
n, m = input().split()
arr = [int(x) for x in input().split()]
a = set([int(y) for y in input().split()])
b = set([int(z) for z in input().split()])

count = [1 if x in a else -1 if x in b else 0 for x in arr]
print(sum(count))