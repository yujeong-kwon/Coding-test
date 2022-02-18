import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    score = list(input().rstrip())
    sum = 0
    cnt = 1
    for j in score:
        if j == "O":
            sum += cnt
            cnt += 1
        elif j == "X":
            cnt = 1
    print(sum)