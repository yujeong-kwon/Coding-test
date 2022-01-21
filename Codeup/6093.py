import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

for i in range(n-1, -1, -1):
    print(a[i], sep=" ")

    #print(a[i], end=" ")