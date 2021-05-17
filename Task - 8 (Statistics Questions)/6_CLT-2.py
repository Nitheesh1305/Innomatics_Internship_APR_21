import math

def cp(x, mu, si):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - mu) / si / math.sqrt(2)))

tickets = int(input())          # 250
students = int(input())         # 100
mu = float(input())              # 2.4   mean
si = float(input())              # 2.0   standard deviation

p = cp(tickets, students * mu, math.sqrt(students) * si)

print("{:.4f}".format(p))