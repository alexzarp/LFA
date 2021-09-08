from pattern import *
import re

arq = open("entrada", "r")
arq = arq.readlines()

epsilon = 'ε'
estado_diposnivel = 0
afnd = [['δ'], ['S']]
afd = []

def print_table(vet):
    for i in range(len(vet)):
        print(vet[i])

def tfn_26(num): # 10 → 26
    numb = []
    if num <= 25:
        return chr(num + 65)

    num = num - 26
    numb.append('A')
    while(True):
        if (num > 25):
            numb[0] = ord(numb[0])
            numb[0]+=1
            numb[0] = chr(numb[0])
            num = num - 26
        elif (num < 0):
            num = num + 26
        else:
            numb.append(chr(num + 65))
            break
    
    numero = ''
    # print(numb)
    for i in range(len(numb)):
        numero = numero + numb[i]

    return numero

# encontra e coloca na tabela os tokens [a-z]
for i in range (len(arq)):
    tokens = re.findall('[a-z]', arq[i])
    for j in range(len(tokens)):
        if tokens[j] in afnd[0]:
            continue
        else:
            afnd[0].append(tokens[j])
simbolos = len(afnd[0])
numero_estados = len(afnd[0]) -1
for j in range(numero_estados):
    afnd[1].append("-")

for i in range(len(arq)):
    estado_atual = re.findall('<[A-Z]>', arq[i])
    for k in range(len(estado_atual)):
        estado_atual[k] = estado_atual[k].replace('<', '')
        estado_atual[k] = estado_atual[k].replace('>', '')
    if estado_atual == []:
        continue # pular os \n
    proximo_estado = re.findall('.<[A-Z]>', arq[i])

    if estado_atual[0] == "S":
        for j in range(len(proximo_estado)):
            proximo_estado[j] = proximo_estado[j].replace('>', '')
            tokens = proximo_estado[j].split('<')
            index = afnd[0].index(tokens[0])
            
            numero = ord(tokens[1])
            numero-=65
            if numero != estado_diposnivel:
                tokens[1] = tfn_26(estado_diposnivel)
            estado_diposnivel+=1

            if afnd[1][index] != '-':
                afnd[1][index].append(tokens[1])
            else:
                afnd[1].insert(index, [tokens[1]])
                afnd[1].pop(index+1)
            afnd.append([tfn_26(estado_diposnivel-1)])
            for j in range(numero_estados):
                afnd[-1].append("-")

        

print_table(afnd)



