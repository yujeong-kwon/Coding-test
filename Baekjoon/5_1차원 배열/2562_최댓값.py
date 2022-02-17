import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    arr.append(int(input().rstrip()))

print(max(arr))
print(arr.index(max(arr)) + 1)

