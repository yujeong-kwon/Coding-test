import sys
input = sys.stdin.readline

arr = []
for i in range(10):
    n = int(input().rstrip())
    arr.append(n%42)
    
arr = set(arr)
print(len(arr))
