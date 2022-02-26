import sys, math
input = sys.stdin.readline

a, b, v = map(int, input().rstrip().split())
day = math.ceil((v-a)/(a-b)) + 1
print(day)
