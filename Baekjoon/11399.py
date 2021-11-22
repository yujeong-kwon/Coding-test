#그리디 - atm기 인출 시간

import sys 
input = sys.stdin.readline

n = int(input().rstrip())
p = list(map(int, input().rstrip().split()))
cal_p = []

p.sort()
num = 0
for i in range(n):
    for j in range(i+1):
        num += p[j]

print(num)
