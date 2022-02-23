import sys
import numpy as np
with open(sys.argv[1], 'r') as fichero:
    linea = fichero.read()

MatrizMin = np.array (linea)
Separar = linea.split('\n')

Separar.pop(0)

MatrizSeparar = []
for i in range(len(Separar)):  
    MatrizSeparar.append (list(Separar[i]))


TamañoMatriz = np.shape(MatrizSeparar)
MatrizCeros= np.zeros(TamañoMatriz)


for i in range(len(MatrizSeparar)):  
    for j in range (len(MatrizSeparar[i])):
        if('*' == MatrizSeparar[i][j]):
            MatrizCeros[i][j] = -1


for i in range(len(MatrizSeparar)):  
    for j in range (len(MatrizSeparar[i])):
        if('*' == MatrizSeparar[i][j]):
            if (j+1) < TamañoMatriz[1] and  (MatrizCeros[i][j+1]) !=-1: #para que no se pasa del valor maximo de fila
                MatrizCeros[i][j+1] += 1 #derecha
            if (j-1) > 0 and (MatrizCeros [i][j-1]) !=-1:
                MatrizCeros [i][j-1] += 1 #Izquierda
            if (i+1) < TamañoMatriz[0] and  (MatrizCeros[i+1][j]) !=-1: #para que no se pasa del valor maximo de fila
                MatrizCeros[i+1][j] += 1 #ABajo
            if (i-1) > 0 and  (MatrizCeros[i-1][j]) !=-1: #para que no se pasa del valor maximo de fila
                MatrizCeros[i-1][j] += 1 #Arriba

            if (i-1) > 0 and (j+1) < TamañoMatriz [1] and (MatrizCeros[i-1][j+1]) !=-1:
                MatrizCeros[i-1][j+1] +=1 #Diagonal derecha arriba
            if (i-1) > 0 and (j-1) > 0 and (MatrizCeros[i-1][j-1]) !=-1:
                MatrizCeros[i-1][j-1] +=1 #Diagonal izquierda arriba
            if (i+1) < TamañoMatriz[0] and (j-1) > 0 and (MatrizCeros[i+1][j-1]) !=-1:
                MatrizCeros[i+1][j-1] +=1 #Diagonal izquierda abajo
            if (i+1) < TamañoMatriz[0] and (j+1) < TamañoMatriz[1] and (MatrizCeros[i+1][j+1]) !=-1:
                MatrizCeros[i+1][j+1] +=1 #Diagonal Derecha abajo


SalidaBuscaminas= MatrizCeros.astype('object')
for i in range(len(SalidaBuscaminas)):  
    for j in range (len(SalidaBuscaminas[i])):
        if(-1 == SalidaBuscaminas[i][j]):
            SalidaBuscaminas[i][j] = '*'


print(SalidaBuscaminas)









       