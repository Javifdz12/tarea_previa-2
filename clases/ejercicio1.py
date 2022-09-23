matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]

for i in range(len(matriz)):
        if matriz[i][0]+matriz[i][1]+matriz[i][2]==matriz[i][3]:
            pass
        else:
            matriz[i]=[matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][0]+matriz[i][1]+matriz[i][2]]
print(matriz)

