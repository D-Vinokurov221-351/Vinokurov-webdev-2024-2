
n = int(input())

matr1 = [[0 for x in range(n)]
            for y in range(n)]
matr2 = [[0 for x in range(n)]
            for y in range(n)]
matr3 = [[0 for x in range(n)]
            for y in range(n)]

for i in range(n):
    for j in range(n):
        a = int(input())
        matr1[i][j] = a

for i in range(n):
    for j in range(n):
        a = int(input())
        matr2[i][j] = a

for i in range(n):
    for j in range(n):
        matr3[i][j] = 0
        for p in range(n):
            matr3[i][j] += (matr1[i][p] * matr2[p][j])

for i in range(n):
    for j in range(n):
        print(matr3[i][j], end=" ")
    print("")