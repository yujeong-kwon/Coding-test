import sys
input = sys.stdin.readline

n = int(input().rstrip())
num = n
count = 0

while True:
    x = (num//10) + (num%10)
    y = ((num%10)*10) + (x%10)
    count += 1
    if y == n:
        break
    num = y

print(count)