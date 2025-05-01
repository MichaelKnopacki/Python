# Exigencia 1
print ("Seja bem vindo, Michael knopacki")

# Exigencia 2
vlr = float(input('Insira o valor unitário: '))
qtd = int(input('Insira a quantidade: '))

desc1 = float(vlr * 0.00)
desc2 = float(vlr * 0.04)
desc3 = float(vlr * 0.07)
desc4 = float(vlr * 0.11)

def multplicador (vlr,qtd):
    return ( vlr * qtd)

print (f'O valor unitário inserido foi {vlr}')
print (f'O a quantidade foi {qtd}')
print ('---------------------------------------------------------------------------------------------------')
if qtd < 2500:
    print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {desc1}')
elif 2500 <= qtd <= 6000 :
    print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {desc2}')
elif 6000 <= qtd <= 10000:
    print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {desc3}')
else :
    print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {desc4}')

print ('---------------------------------------------------------------------------------------------------')
print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {multplicador(vlr,qtd)}')
