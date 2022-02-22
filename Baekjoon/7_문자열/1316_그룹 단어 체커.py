import sys 
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0 
for _ in range(n):
    word = input().rstrip()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new = word[i+1:]
            if new.count(word[i]) == 0:
                cnt += 1
print(cnt)