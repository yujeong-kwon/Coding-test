import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    arr = list(input().rstrip())
    for i in range(2, len(arr)):
        print(int(arr[0])*arr[i], end='')
        
    print()
