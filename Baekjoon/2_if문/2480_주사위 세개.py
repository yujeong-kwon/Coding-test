import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
if a==b and b==c :
    m = 10000 + a * 1000
elif a==b or b==c:
    m = 1000 + b * 100
elif a==c:
    m = 1000 + a * 100
else:
    m = max(a,b,c) * 100

print(m)