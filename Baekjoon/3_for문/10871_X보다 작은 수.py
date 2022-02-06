import sys 
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
num = list(map(int, input().rstrip().split()))
result = []
for i in num:
    if i < x:
        result.append(i)
for i in result:
    print(i, end = ' ')