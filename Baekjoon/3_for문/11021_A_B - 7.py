import sys
input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    a, b = map(int,input().rstrip().split())
    print("Case #" + str(i+1) + ": " + str((a+b)))