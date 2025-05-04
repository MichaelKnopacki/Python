# Exigencia A
print ("Seja bem vindo, Felipe Eduardo Laurentino Ribeiro")

# Exigencia B
vlr = float(input('Insira o valor unitário: '))
qtd = int(input('Insira a quantidade: '))

vlrTotal = float(vlr*qtd)
desc1 = float(vlrTotal * 0.00)
desc2 = float(vlrTotal * 0.04)
desc3 = float(vlrTotal * 0.07)
desc4 = float(vlrTotal * 0.11)


print (f'O valor unitário inserido foi {vlr}')
print (f'O a quantidade foi {qtd}')
print ('---------------------------------------------------------------------------------------------------')
# Exigencia D
print (f'O valor final SEM desconto da compra e {vlr} X {qtd}, totalizando R$ {vlrTotal}')
print ('---------------------------------------------------------------------------------------------------')
# Exigencia C, D & E
if vlrTotal < 2500:
    print (f'O valor final COM desconto da compra e {vlr} X {qtd}, totalizando um desconto de R$ {desc1}. O valor final do produto ficou em {vlrTotal-desc1}')
elif 2500 <= vlrTotal <= 6000 :
    print (f'O valor final COM desconto da compra e {vlr} X {qtd}, totalizando um desconto de R$ {desc2}. O valor final do produto ficou em {vlrTotal-desc2}')
elif 6000 <= vlrTotal <= 10000:
    print (f'O valor final COM desconto da compra e {vlr} X {qtd}, totalizando um desconto de R$ {desc3}. O valor final do produto ficou em {vlrTotal-desc3}')
else :
    print (f'O valor final COM desconto da compra e {vlr} X {qtd}, totalizando um desconto de R$ {desc4}. O valor final do produto ficou em {vlrTotal-desc4}')
