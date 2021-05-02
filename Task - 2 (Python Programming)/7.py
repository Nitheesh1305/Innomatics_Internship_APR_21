#Question 7 - Introduction To Sets

import statistics
def average(array):
    return(statistics.mean(list(set(array))))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)