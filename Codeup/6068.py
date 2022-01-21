import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n>=90 and n<=100:
    print("A")
elif n>=70 and n<90:
    print("B")
elif n>=40 and n<=70:
    print("C")
else:
    print("D")


#if n>=90:
#    print("A")
#else:
#    if n>=70:
#        print("B")
#    else:
#        if n>=40:
#            print("C")
#        else:
#            print("D")
        