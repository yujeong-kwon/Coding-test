import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=" ")

# 0이 들어간 24개의 칸으로 이루어진 리스트 생성
# 입력 받은 n 개의 수의 인덱스의 값을 1씩 증가 
# 1번부터 23번까지 24명의 불린 수를 출력