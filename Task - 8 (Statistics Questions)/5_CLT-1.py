import math

def cp(x, mu, si):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - mu) / si / math.sqrt(2)))

capacity = float(input())       # 9800  maximum load
n = int(input())                # 49    number of boxes
mu = float(input())              # 205   mean
si = float(input())              # 15    standard deviation

p = cp(capacity, n * mu, math.sqrt(n) * si)

print("{:.4f}".format(p))