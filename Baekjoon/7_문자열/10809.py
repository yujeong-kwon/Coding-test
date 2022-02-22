import sys
input = sys.stdin.readline

word = input().rstrip()
result = []

for i in range(97, 123) :
  result.append(str(word.find(chr(i))))

print(" ".join(result))

#유빈이 코드임