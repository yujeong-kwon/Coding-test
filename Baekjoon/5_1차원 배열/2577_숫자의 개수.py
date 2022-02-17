import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

#문자열로 만들어서 리스트처럼 접근
mul = str(a * b * c)
result = [0] * 10
for i in mul:
    result[int(i)] += 1
for i in result:
    print(i)
            

