import sys
input = sys.stdin.readline

#무조건 3과목이 아니다 -> 런타임 에러 세과목만 받으려했음
n = int(input().rstrip())
score = list(map(int, input().rstrip().split()))
m = max(score)

new = []
for i in score:
    new.append(i / m * 100)

print(sum(new)/n)