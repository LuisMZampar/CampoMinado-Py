import random

def cria_matriz(valor):
    matriz = []
    for i in range(10):
        matriz.append([valor] * 10)
    return matriz

def imprime(mat):
    for linha in mat:
        st = ""
        for valor in linha:
            if valor == 0:
                st = st + " _"
            elif valor == -1:
                st = st + " B"
            else:
                st = st + " " + str(valor)
        print(st)


def coloca_bomba(mat):
    qtd_bomba = 0
    while qtd_bomba < 10:
        i = random.randint(0, 9)
        j = random.randint(0, 9)
        if mat[i][j] == 0:
            mat[i][j] = -1
            qtd_bomba = qtd_bomba + 1        

#retorna uma lista contendo tuplas que 
# indicam as posicoes vizinhas de (lin, col) 
def retorna_vizinhos(lin, col):
    lista = []
    if lin > 0 and col > 0:
        lista.append([lin-1, col-1])
    if lin > 0:
        lista.append([lin-1, col])        
    if lin > 0 and col < 9:
        lista.append([lin-1, col+1])

    if col > 0:
        lista.append([lin, col-1])
    if col < 9:
        lista.append([lin, col+1])

    if lin < 9 and col > 0:
        lista.append([lin+1, col-1])
    if lin < 9:
        lista.append([lin+1, col])
    if lin < 9 and col < 9:
        lista.append([lin+1, col+1])
    
    return lista

def coloca_numeros(mat):
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 0:
                viz = retorna_vizinhos(i, j)
                for [x, y] in viz:
                    if mat[x][y] == -1:
                        mat[i][j] = mat[i][j] + 1

def mostra_campo(mtab, mesp):
    for i in range(10):
        st = ""
        for j in range(10):
            if mesp[i][j] == False:
                st = st + " _"
            elif mtab[i][j] == 0:
                st = st + "  "
            elif mtab[i][j] == -1:
                st = st + " *"
            else:
                st = st + " " + str(mtab[i][j])
        print(st)

#MAIN
if __name__ == '__main__':
    mat_tab = cria_matriz(0)
    mat_esp = cria_matriz(False)

    coloca_bomba(mat_tab)
    coloca_numeros(mat_tab)
    #imprime(mat_tab)
    mostra_campo(mat_tab, mat_esp)

    i = int(input("Informe a linha: "))
    j = int(input("Informe a coluna: "))
    mat_esp[i][j] = True

    if mat_tab[i][j] == -1:
        print("Explodiu!")
    elif mat_tab[i][j] == 0:
        #aqui achamos uma posicao 0
        posicoes = []
        posicoes.append( [i, j] )    
        
        while len(posicoes) != 0:
            pos = posicoes.pop(0)
            viz = retorna_vizinhos(pos[0], pos[1])
            for [x, y] in viz:
                if mat_esp[x][y] == False:
                    mat_esp[x][y] = True
                    if mat_tab[x][y] == 0:
                        posicoes.append( [x, y] )

    mostra_campo(mat_tab, mat_esp)
    print("##############")
    imprime(mat_tab)