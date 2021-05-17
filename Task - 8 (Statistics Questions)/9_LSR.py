
def pearson(n, X, Y):
    mx = sum(X) / n                
    my = sum(Y) / n

    sx = 0.
    sy = 0.
    p = 0.

    for x, y in zip(X, Y):
        sx += (x - mx) ** 2         
        sy += (y - my) ** 2        
        p += (x - mx) * (y - my)    

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    p = p / (n * sx * sy)

    b = p * sy / sx                 # Y = a + b X
    a = my - b * mx

    return p, a, b


X, Y = [0] * 5, [0] * 5
for i in range(5):
    X[i], Y[i] = map(int, input().split())

_, a, b = pearson(5, X, Y)

print("{:.3f}".format(a + b * 80))