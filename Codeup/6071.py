import sys
input = sys.stdin.readline

#처음 조건 검사를 통과하기 위해 0이 아닌 값을 임의로 저장
n = 1
while n!=0:
    n = int(input().rstrip())
    if n!=0:
        print(n)