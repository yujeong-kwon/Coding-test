import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))

print(min(arr), max(arr))
