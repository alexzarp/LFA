from pattern import *

arq = open("entrada", "r")
arq = arq.readlines()

afnd = [['δ'], ['S']]
afd = []
# contatos = {'Yan': '1234-5678'}
# numeracao_minuscula = [("a", 0), ("b", 1), ('d', 2), ('e', 3), ('f', 4), ('g', 5), ('h', 6), ('i', 7), ('j', 8), ('k', 9), ('l', 10), ('m', 11), ('n', 12), ('o', 13), ('p', 14), ('q', 15), ('r', 16), ('s', 17), ('t', 18), ('u', 19), ('v', 20), ('w', 21), ('y', 22), ('k', 23), ('x', 24), ('z', 25)]
# contatos = dict(numeracao_minuscula)
    
# print( ord('a'),chr(1+96))

# afnd
for i in range (len(arq)):
    tokens = re.findall('[a-z]', arq[i])
    for j in range(len(tokens)):
        if tokens[j] in afnd[0]:
            break
        else:
            afnd[0].append(tokens[j])
afnd[0].sort()
afnd[0].insert(0, afnd[0][-1])
afnd[0].pop(-1)
print(afnd)
