import sys
input = sys.stdin.readline

day = 1
a, b, c = map(int, input().rstrip().split())

while day%a!=0 or day%b!=0 or day%c!=0:
    day += 1

print(day)
