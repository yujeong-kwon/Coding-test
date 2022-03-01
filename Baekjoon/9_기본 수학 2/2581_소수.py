import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())

nums = [i for i in range(m, n+1)]
result = []
cnt = 0
for i in nums:
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            cnt += 1
            result.append(i)
if cnt == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
