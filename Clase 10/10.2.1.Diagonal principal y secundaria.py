N=int(input())
l=[]
for i in range (N):
    temp=list(map(int,input().split()))
    l.append(temp)
#print(l)

diagonal_principal=[]
diagonal_secundaria=[]

for i in range(len(l)):
    for j in range(len(l[i])):
        #print(f"Valor en la posición ({i}, {j}): {1[1][5]}")
        if i == j:
            #print(f"Valor de la posición ({i),{j}): {l[i][5]}")
            diagonal_principal.append(l[i][j])
        if i + j == len(l)-1:
            diagonal_secundaria.append(l[i][j])

print(diagonal_principal)
print(diagonal_secundaria)

