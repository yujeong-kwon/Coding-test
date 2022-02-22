import sys
input = sys.stdin.readline

#i를 str로 바꾸고 map으로 정수로 변환해 list에 저장 
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

#복습