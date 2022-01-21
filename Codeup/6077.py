import sys
input = sys.stdin.readline

n = int(input().rstrip())
i = 0
s = 0

while i <= n:
    if i % 2 == 0:
        s += i
    i += 1

print(s)

