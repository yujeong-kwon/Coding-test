import sys
input = sys.stdin.readline

h, m = map(int, input().rstrip().split())
t = int(input().rstrip())

h += t // 60
m += t % 60

if m >= 60:
    h += 1
    m -= 60
    
if h >= 24:
    h -= 24

print(h, m)
