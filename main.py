matriz = [[1,1,2,9],
           [2,4,-3,1],
           [3,6,-5,0]
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


       return 


metodo_gaus(matriz)




