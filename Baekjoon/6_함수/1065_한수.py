import sys
input = sys.stdin.readline


def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        i = str(i)
        if int(i)<100:
            cnt += 1
        elif int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]) :
            cnt += 1
    return cnt

print(hansu(int(input().rstrip())))
