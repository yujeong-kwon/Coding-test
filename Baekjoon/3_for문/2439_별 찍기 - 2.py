import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(1, n+1):
    print(("*" * i).rjust(n))