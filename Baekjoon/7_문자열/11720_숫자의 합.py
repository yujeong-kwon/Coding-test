#1
import sys
input = sys.stdin.readline

n = input().rstrip()
n_list = list(map(int,str(input().rstrip())))

sum = 0
for i in n_list:
    sum += i

print(sum)

#2
n = input()
num = str(input())

result = 0
for i in num:
    result += int(i)

print(result)

#3
n = int(input())
num = input()

result = 0
for i in range(n):
    result += int(num[i])

print(result)