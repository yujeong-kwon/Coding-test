import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range (t):
    a, b = map(int,input().rstrip().split())
    print("Case #%s: %s + %s = %s"%(i+1, a, b, (a+b)))