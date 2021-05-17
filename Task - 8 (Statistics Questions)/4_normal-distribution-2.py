import math

def N(x, mu, si):
    """ Normal Distribution """
    pie = math.pi
    return math.exp(- (x - mu) ** 2 / (2 * si * si)) / (si * math.sqrt(2 * pie))



def cp(x, mu, si):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - mu) / si / math.sqrt(2)))


mu, si = map(float, input().split())
q1 = float(input())
q2 = float(input())

# percentage of students having grade > q1
print("{:.2f}".format(100 - cp(q1, mu, si) * 100))

# percentage of students having grade ≥ q2
print("{:.2f}".format(100 - cp(q2, mu, si) * 100))

# percentage of students having grade < q2
print("{:.2f}".format(cp(q2, mu, si) * 100))