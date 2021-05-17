import math

pie = math.pi


def N(x, mu, si):
    """ Normal Distribution """
    return math.exp(- (x - mu) ** 2 / (2 * si * si)) / (si * math.sqrt(2 * pie))


def cp(x, mu, si):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - mu) / si / math.sqrt(2)))


mu = 20
si = 2

print("{:.3f}".format(cp(19.5, mu, si)))

print("{:.3f}".format(cp(22, mu, si) - cp(20, mu, si)))