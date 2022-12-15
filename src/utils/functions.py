from pandas import DataFrame as pDF
def lerMedidas(medida:str):
    tabela = pDF([linhas.strip().split(',') for linhas in open('src/constants/tipos/'+medida+'.txt').readlines()])
    medidas = pDF(tabela[1].values,index=tabela[0].values,columns=['simbolo'])
    medidas.insert(1,'constante', [int(tabela[2][i])/int(tabela[3][i]) for i in range(len(tabela[1]))])
    return medidas

def lerPotencias():
    tabela = pDF([linhas.strip().split(',') for linhas in open('src/constants/potencias.txt').readlines()])
    medidas = pDF([[tabela[1][i],tabela[2][i]] for i in range(len(tabela[1]))],index=tabela[0].values,columns=['simbolo','exp10'])
    return medidas 

def convertZeros(unidade:str):
    if '³' in unidade: return 3
    elif '²' in unidade: return 2
    else: return 1

def pegarTipos():
    tipos = [linhas.strip() for linhas in open('src/constants/tipos.txt').readlines()]
    return tipos

def arrumar(numero:str):return float(numero.replace(',','.'))

def desarrumar(numero:float):return str(round(numero,3)).replace('.', ',')
    