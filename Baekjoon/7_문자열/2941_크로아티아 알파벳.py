import sys 
input = sys.stdin.readline

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()
for i in cro:
    if i in word:
        word = word.replace(i, "_")

print(len(word))


#if i in word 는 없어도됨