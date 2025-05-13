#[EXIGÊNCIA DE CÓDIGO 1 de 8];
print ("Seja bem vindo a Loja de Gelados do ")
print ("Felipe Eduardo Laurentino Ribeiro")
print ('-----------------Cardápio-----------------')
print ('------------------------------------------')
print ('---| Tamanho | Cupuacu (CP) | Açaí (AC)---|')
print ('---|    P    |   R$ 9.00    |  R$ 11.00---|')
print ('---|    M    |   R$ 14.00   |  R$ 16.00---|')
print ('---|    G    |   R$ 18.00   |  R$ 20.00---|')
print ('------------------------------------------')

total = 0
while True:
    #[EXIGÊNCIA DE CÓDIGO 6 de 8];
    while True :
        #[EXIGÊNCIA DE CÓDIGO 2 de 8];
        sabor = input('Insira um sabor desejado CP/AC : ').upper()
        if sabor != 'CP' and sabor != 'AC':
            print( 'Sabor inválido. Tente novamente. ')
            continue

        #[EXIGÊNCIA DE CÓDIGO 3 de 8];
        tamanho = input('Insira o tamanho desejado, sendo eles : P = Pequeno, M = Médio e G = Grande : ').upper()
        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print ('Tamanho inválido. Tente novamente. ')
            continue
        break

    print ('----------------------------------------------------------------------------')

    #[EXIGÊNCIA DE CÓDIGO 4 de 8];
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9
            print('O valor é R$ 9,00')
        elif tamanho == 'M':
            valor_pedido = 14
            print('O valor é R$ 14,00')
        elif tamanho == 'G':
            valor_pedido = 18
            print('O valor é R$ 18,00')
    elif sabor == 'AC':
        if tamanho == 'P':
            valor_pedido = 11
            print('O valor é R$ 11,00')
        elif tamanho == 'M':
            valor_pedido = 16
            print('O valor é R$ 16,00')
        elif tamanho == 'G':
            valor_pedido = 20
            print('O valor é R$ 20,00')
    #[EXIGÊNCIA DE CÓDIGO 5 de 8];
    total += valor_pedido


    print ('----------------------------------------------------------------------------')

    #[EXIGÊNCIA DE CÓDIGO 6 de 8];
    resposta = input ('Deseja mais alguma coisa? (S/N) ').upper()
    if resposta == 'N':
        break
    print ('----------------------------------------------------------------------------')

print (f'Valor total do pedido R$ : {total}')
     