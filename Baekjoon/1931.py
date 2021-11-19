import sys 
input = sys.stdin.readline

n = int(input().rstrip())


time=[]
for _ in range(n):
    time.append(list(map(int,input().rstrip().split())))

time.sort(key=lambda x: (x[1], x[0]))

#for문에서 요소 2개 쓸 수 있음
count = 0
last_time = 0

for start, end in time:
    if last_time <= start:
        last_time = end
        count += 1

print(count)
