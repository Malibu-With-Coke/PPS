a = list(map(int, input().split()))
N = int(a[0])
feel = int(a[1])

b = list(map(int, input().split()))

q = int(b[0])    # G > G
w = int(b[1])    # G > B
e = int(b[2])    # B > G
r = int(b[3])    # B > B

preG = []
preB = []

if feel==0:
    preG[0] = q
    preB[0] = w
else:
    preG[0] = e
    preB[0] = r

for i in range(1,len(N)):
    preG[i] = preG[i-1]*q +preB[i-1]*e
    preB[i] = preG[i-1]*w +preB[i-1]*r

print(round(preG[i-1]*1000))
print(round(preB[i-1]*1000))