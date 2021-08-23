from pattern import *
import re

arq = open("entrada", "r")
arq = arq.readlines()

epsilon = 'ε'
afnd = [['δ']]
afd = []

# numeracao_minuscula = [("A", 0), ("b", 1), ("C", 2), ('d', 2), ('e', 3), ('f', 4), ('g', 5), ('h', 6), ('i', 7), ('j', 8), ('k', 9), ('l', 10), ('m', 11), ('n', 12), ('o', 13), ('p', 14), ('q', 15), ('r', 16), ('s', 17), ('t', 18), ('u', 19), ('v', 20), ('w', 21), ('y', 22), ('k', 23), ('x', 24), ('z', 25)]
# contatos = dict(numeracao_minuscula)

def print_table(vet):
    for i in range(len(vet)):
        print(vet[i])
# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
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
# afnd[0].sort()
# afnd[0].insert(0, afnd[0][-1])
# afnd[0].pop(-1)

# encontra e coloca na tabela os tokens <[A-Z]>
for i in range (len(arq)):
    tokens = re.findall('<[A-Z]>', arq[i])
    ep = re.findall(epsilon, arq[i])
    if tokens != []:
        if ep != []:
            afnd.append(['*' + tokens[0]])
        else:
            afnd.append([tokens[0]])


# cont = len(afnd[0]) -1
# for i in range (len(arq)):
# print_table(afnd)
n = int(input("Digite o numero: "))
print(tfn_26(n))
