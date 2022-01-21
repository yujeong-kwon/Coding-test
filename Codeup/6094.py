import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

least = a[0]

for i in range(1, n):
    if least > a[i]:
        least = a[i]

print(least)
