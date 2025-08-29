matriz3x3 = [               #  [       
              [1,1,2,9],    #     [ 3 , 6 , -5, 0 ],
              [2,4,-3,1],   #     [ 2 , 4 , -3,-1 ],
              [3,6,-5,0]    #     [ 1 , 1 , 2 , 9 ]
            ]               #   ]       
matriz10x10 = [
                [ 2 ,  3 , -1 ,  4 ,  1 , -2 ,  1 ,  5 , -3 ,  1 ],
                [ 1 , -4 ,  2 ,  3 , -1 ,  1 ,  2 , -1 ,  4 , -2 ],
                [ 3 ,  1 ,  1 , -2 ,  5 ,  1 , -3 ,  2 , -1 ,  4 ],
                [ 4 , -1 ,  3 ,  2 , -1 ,  2 ,  1 , -3 ,  5 , -1 ],
                [ 1 ,  2 , -3 ,  1 ,  4 , -1 ,  2 , -1 ,  3 ,  2 ],
                [ 2 , -1 ,  4 , -2 ,  3 ,  1 , -5 ,  2 ,  1 , -4 ],
                [ 1 ,  3 ,  2 , -1 , -2 ,  4 ,  1 , -3 ,  2 ,  1 ],
                [ 5 , -2 ,  1 ,  3 ,  1 , -1 ,  2 ,  4 , -2 ,  3 ],
                [ 3 ,  1 , -2 ,  4 ,  1 ,  2 , -1 , -1 ,  5 , -3 ],
                [ 2 ,  4 ,  1 , -1 ,  3 , -2 ,  1 ,  2 , -1 ,  1 ]
              ]

def metodo_gaus(matriz):
       
#  =========  Fazendo o pivotamento parcial (achando o maior numero da primeira coluna). ========= #

       aux = 0
       pivo = 0
       indicie = 0
       
       for i in range(len(matriz)):
            aux = matriz[i][0]
              
            if (pivo < aux) :
                    pivo = aux
                    indicie = i       
       
       matriz_aux = matriz[0]
       matriz[0] = matriz[indicie]
       matriz[indicie] = matriz_aux

       print(matriz)
       
#  =========  Fazendo as operações nas linhas utilizando o pivo. ========= #

       for i in range(len(matriz)):
            for j in range(len(matriz) - (i+1) ):
                  for k in range(len(matriz[0])):
                      m = matriz[j+1+i][i]/matriz[i][i]
                      matriz[j+1+i][k] -= m * matriz[i][k]

       return print(matriz)


metodo_gaus(matriz10x10)





