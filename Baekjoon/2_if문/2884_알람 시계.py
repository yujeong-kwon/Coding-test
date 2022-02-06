H, M = map(int,input().split())

if M < 45:
     M = M + 60 - 45
     if H == 0:
        H = 23 
     elif H > 0:
        H -= 1
elif M >= 45:
    M = M - 45

print(H, M, sep = " ")