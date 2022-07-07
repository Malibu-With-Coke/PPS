def sum__(n):            # 각 자리 숫자의 합 더함.
    N=[int(i) for i in str(n)]
    return sum(N)

n = int(input())
check = 0
for  i in range(1,n):
    if n == i + sum__(i):
        check = i
        break
    
if (check):
    print(check)
else:
    print(0)