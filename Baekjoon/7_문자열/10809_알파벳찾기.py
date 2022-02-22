import sys
input = sys.stdin.readline

all = "abcdefghijklmnopqrstuvwxyz"
find_str = input().rstrip()

for i in all:
    print(find_str.find(i), end=" ")


#인덱스랑 -1을 result에 넣을 필요없이 바로 출력
#print(' '.join(result))


#TypeError: sequence item 0: expected str instance, int found
#''.join(list_name)을 쓸 때, list의 모든 element들은 문자여야 한다. 
# 즉 list에 저장된 값이 정수이거나 실수이면 이와 같은 에러가 뜰 것이다.

#TypeError: 'str' object is not callable
#위에서 변수를 str로 지정


#코드
""" 

all = list(range(97,123))  # 아스키코드 숫자 
find_str = input().rstrip()

for i in all :
    print(find_str.find(chr(i))) 
"""

#많이 틀렸던건 알파벳을 잘못 저장했음,,