T = int(input())
a = [0] * T
b = [0] * T
for i in range(T):
    a[i], b[i] = map(int,input().split())
for i in range(T):
    print(a[i]+b[i])