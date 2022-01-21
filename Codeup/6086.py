import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = 0
i = 0

while s < n:
    i += 1
    s += i

print(s)
