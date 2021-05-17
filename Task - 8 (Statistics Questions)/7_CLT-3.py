import math

n = int(input())                # 100       sample size
mu = float(input())              # 500       mean
si = float(input())              # 80        standard deviation
percent = float(input())        # 0.95      distribution percentage we want to cover
z = float(input())              # 1.96      z-score : Φ(1.96) - Φ(-1.96) ≈ 95%

e = z * si / math.sqrt(n)
print('{:2f}'.format(mu - e))
print('{:2f}'.format(mu + e))