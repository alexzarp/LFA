from pattern import *

arq = open("entrada", "r")
arq = arq.readlines()

epsilon = 'ε'
afnd = [['δ']]
afd = []
# contatos = {'Yan': '1234-5678'}
# numeracao_minuscula = [("a", 0), ("b", 1), ('d', 2), ('e', 3), ('f', 4), ('g', 5), ('h', 6), ('i', 7), ('j', 8), ('k', 9), ('l', 10), ('m', 11), ('n', 12), ('o', 13), ('p', 14), ('q', 15), ('r', 16), ('s', 17), ('t', 18), ('u', 19), ('v', 20), ('w', 21), ('y', 22), ('k', 23), ('x', 24), ('z', 25)]
# contatos = dict(numeracao_minuscula)
    
# print( ord('a'),chr(1+96))

# encontra e coloca na tabela os tokens [a-z]
for i in range (len(arq)):
    tokens = re.findall('[a-z]', arq[i])
    for j in range(len(tokens)):
        if tokens[j] in afnd[0]:
            continue
        else:
            afnd[0].append(tokens[j])
afnd[0].sort()
afnd[0].insert(0, afnd[0][-1])
afnd[0].pop(-1)
# print(afnd)

# encontra e coloca na tabela os tokens <[A-Z]>
for i in range (len(arq)):
    tokens = re.findall('<[A-Z]>', arq[i])
    ep = re.findall(epsilon, arq[i])
    if tokens != []:
        if ep != []:
            afnd.append(['*' + tokens[0]])
        else:
            afnd.append([tokens[0]])
print(afnd)