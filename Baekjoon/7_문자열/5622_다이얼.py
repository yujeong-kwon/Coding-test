import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input().rstrip()
sum = 0
for i in dial:
    for j in range(len(a)):
        if a[j] in i:
            sum += dial.index(i) + 3

print(sum)

#복습