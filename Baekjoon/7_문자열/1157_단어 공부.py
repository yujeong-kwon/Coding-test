import sys
input = sys.stdin.readline

word = input().rstrip().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    word_cnt = word.count(i)
    cnt.append(word_cnt)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(word_list[max_index])
    
#복습 필요!!