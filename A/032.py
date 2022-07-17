def apart(n,k):
    sum = 0
    if n==1:
        return 1
    elif k==0:
        return n
    else:
        for i in range(n,0,-1):
            sum += apart(i,k-1)
        return sum

n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    print(apart(n,k))