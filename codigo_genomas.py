def split_data(archivos,lista_genomas_titulos):

    for i in lista_genomas_titulos:
        data_genomas.append(str(''.join(str(i.read()).split('\n')[1:])).replace('\n',''))



def obtener_resultados(data_genomas,matriz_final):
    posi = 0
    posj = 0
    for lista1 in data_genomas:
        for lista2 in data_genomas: 
            contador_letras = 0
            tam_min=min(len(lista1),len(lista2))
            for letra in range(0,tam_min):
                if lista2[letra]==lista1[letra]:
                    contador_letras+=1
            matriz_final[posi][posj]=round((contador_letras/len(lista2)*100),3)
            posj+=1
        posj=0
        posi+=1 


def generar_tabla(matriz_final,archivos):

    space_len = 16 
    split_name = 8 
    print(" "*space_len,"|",end='')
    for nombre in archivos:
        print("|",end='')
        print ((nombre[split_name:]).center(space_len),end=' ')
        print("|",end='')
    print('\n')

    posi = 0

    for lista1 in matriz_final:
        print((archivos[posi])[split_name:].center(space_len),end=' ')
        for lista2 in lista1:
            print("|",end='')
            print((str(lista2).center(space_len)),end=' ')
            print("|",end='')
        print('\n')
        posi+=1


archivos = ["genomas/AY274119.txt",
            "genomas/AY278488.2.txt",
            "genomas/MN908947.txt",
            "genomas/MN988668.txt",
            "genomas/MN988669.txt"]

lista_genomas_titulos = [open(x) for x in archivos]

matriz_final=[[0]*len(archivos) for i in range(0,len(archivos))]

data_genomas = []

split_data(archivos,lista_genomas_titulos)

obtener_resultados(data_genomas,matriz_final)

generar_tabla(matriz_final,archivos)

