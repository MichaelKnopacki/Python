# Exigencia A
print ("Seja bem vindo a Loja de Gelados do ")
print ("Felipe Eduardo Laurentino Ribeiro")
print ('-----------------Cardápio-----------------')
print ('------------------------------------------')
print ('---| Tamanho | Cupuacu (CP) | Açaí (AC)--|')
print ('---|    P    |   R$ 9.00    |  R$ 11.00--|')
print ('---|    M    |   R$ 14.00   |  R$ 16.00--|')
print ('---|    G    |   R$ 18.00   |  R$ 20.00--|')
print ('------------------------------------------')



while True :
    sabor = input('Insira um sabor desejado CP/AC : ').upper()
    tamanho = input('Insira o tamanho desejado, sendo eles : P = Pequeno, M = Médio e G = Grande : ').upper()
    if sabor != 'CP' and sabor != 'AC':
        print( 'Sabor inválido. Tente novamente. ')
        continue
    elif tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print ('Tamanho inválido. Tente novamente. ')
    continue
    break

print ('----------------------------------------------------------------------------')

if sabor == 'CP' or sabor == 'AC' and tamanho == 'P' :
    print (' O valor é R$ 11,00 ')
elif sabor == 'CP' or sabor == 'AC' and tamanho == 'M' :
    print (' O valor é R$ 11,00 ')
elif sabor == 'CP' or sabor == 'AC' and tamanho == 'G' :
    print (' O valor é R$ 16,00 ')
else :
    print(' Sabor/Tamanho inválido')

print ('----------------------------------------------------------------------------')