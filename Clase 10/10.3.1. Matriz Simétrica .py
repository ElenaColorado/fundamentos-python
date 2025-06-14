N = int(input())
l = []

for i in range(N):
    temp = list(map(int, input().split(',')))
    l.append(temp)

simetrica = True
for i in range(N):
    for j in range(N):
        if l[i][j] != l[j][i]:
            simetrica = False

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
