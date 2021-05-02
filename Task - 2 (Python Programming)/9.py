#Question 9 - Symmetric Difference

a = input()
N = list(map(int, input().split()))
b = input()
M = list(map(int, input().split()))

s_diff = []


s_diff.append(list(set(N).difference(set(M))))
s_diff.append(list(set(M).difference(set(N))))

s_diff = [item for sublist in s_diff for item in sublist]

for i in sorted(s_diff):
    print(i)