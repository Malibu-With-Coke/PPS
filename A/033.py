max = 0
max_i = 0
sum = []
for i in range(5):
    n1,n2,n3,n4 = map(int ,input().split())
    sum.append(n1 + n2 + n3 + n4)
    if max < sum[i]:
        max = sum[i]
        max_i = i

print(max_i+1,max)