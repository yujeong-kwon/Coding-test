#그리디 - 잃어버린 괄호(적당히 괄호 넣어 최솟값구하기)
import sys 
input = sys.stdin.readline

a = list(input().rstrip().split('-'))
result = []
for i in a:
    new_b = 0
    b = i.split('+')
    for j in b:
        new_b += int(j)
    result.append(new_b)
num = result[0]
for i in range(1,len(result)):
    num -= result[i]

print(num)
