import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))
for i in arr:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
