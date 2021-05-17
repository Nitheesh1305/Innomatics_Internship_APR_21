from math import factorial


def b(n, x, p):
    return factorial(n) // factorial(n - x) // factorial(x) * (p ** x) * (1 - p) ** (n - x)

p, n = map(int, input().split())

p = p / 100     

r = b(n, 0, p) + b(n, 1, p) + b(n, 2, p)     
print("%.3f" % r)

r = sum(b(n, i, p) for i in range(2, n + 1))    
print("%.3f" % r)