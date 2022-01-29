def gridTravellar(m,n):
    table = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        table[i][0] = 1
    for j in range(n):
        table[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]
ans = gridTravellar(2,3)
print(ans)