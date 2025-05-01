# Exigencia 1
print ("Seja bem vindo, Michael knopacki")

# Exigencia 2
vlr = float(input('Insira o valor unitário: '))
qtd = int(input('Insira a quantidade: '))

desc1 = float(0.00)
desc2 = float(0.04)

def multplicador (vlr,qtd):
    return ( vlr * qtd)

print (f'O valor unitário inserido foi {vlr}')
print (f'O a quantidade foi {qtd}')
print ('---------------------------------------------------------------------------------------------------')
if qtd < 2500:
    print ('Primeira condicao, 0%')
elif 2500 <= qtd <= 6000 :
    print ('Segunda condicao, 4%')
elif 6000 <= qtd <= 10000:
    print(' Terceira condicao, 7% ')
else :
    print('Quarta condicao, 11%')

print ('---------------------------------------------------------------------------------------------------')
print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {multplicador(vlr,qtd)}')
