from re import I
import sys
input = sys.stdin.readline

n = int(input().rstrip())
i = 0
s = 0

while s < n:
    i += 1
    s += i
    

print(i)
