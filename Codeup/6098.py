import sys
input = sys.stdin.readline

m = [[0 for i in range(12)] for i in range(12)]

for i in range(10):
    #map은 리스트처럼 접근할 수 없어서 list로 만들어야된다
    a = list(map(int, input().rstrip().split()))
    for j in range(10):
        m[i+1][j+1] = int(a[j])

x = 2
y = 2

while True:
    #계속 진행
    if m[x][y] == 0:
        m[x][y] = 9
    #break는 반복문 종료
    elif m[x][y] == 2:
        m[x][y] = 9
        break
    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9):
        break

    if m[x][y+1] != 1:
        y += 1
    elif m[x+1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(m[i][j], end=" ")
    print()