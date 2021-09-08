def tfn_26(num): # 10 → 26
    numb = []
    if num <= 25:
        return chr(num + 65)

    num = num - 26
    numb.append('A')
    while(True):
        if (num > 25):
            if (num > 701):
                

            else:
                if (len(numb) > 1):
                    numb[-2] = ord(numb[-2])
                    numb[-2]+=1
                    numb[-2] = chr(numb[-2])
                else:
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

i = 0
while(i < 702):
    print(tfn_26(i))
    i+=1