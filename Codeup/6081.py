import sys
input = sys.stdin.readline

str = int(input().rstrip(), 16)

for i in range(1, 16):
    print('%X'%str, '*%X'%i, '=%X'%(str*i), sep='')

#print("%X*%X=%X" %(str,i,str*i))