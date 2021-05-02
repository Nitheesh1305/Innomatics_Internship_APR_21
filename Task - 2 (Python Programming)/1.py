#Question 1 : List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(j + 1) if x + y + z != n])
