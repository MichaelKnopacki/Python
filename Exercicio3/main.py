# [EXIGÊNCIA DE CÓDIGO 1 de 7]
print('Seja bem vindo a copiadora do Felipe Eduardo Laurentino Ribeiro')

# [EXIGÊNCIA DE CÓDIGO 2 de 7]
def escolha_servico():
    while True:
        servico = input("Escolha o serviço (DIG / ICO / IPB / FOT): ").upper()
        if servico == 'DIG':
            valor_unitario = 1.10
            print("Serviço selecionado: Digitalização. Valor R$ 1.10 por página")
            return valor_unitario
        elif servico == 'ICO':
            print("Serviço selecionado: Impressão Colorida. Valor R$ 1.00 por página")
            valor_unitario = 1.00
            return valor_unitario
        elif servico == 'IPB':
            print("Serviço de Impressão Preto e Branco. Valor R$ 0.40 por página")
            valor_unitario = 0.40
            return valor_unitario
        elif servico == 'FOT':
            print("Serviço de Fotocópia")
            valor_unitario = 0.20
            return valor_unitario
        else:
            print("Serviço inválido. Tente novamente.")

# [EXIGÊNCIA DE CÓDIGO 3 de 7]
def num_pagina():
    while True:
        # [EXIGÊNCIA DE CÓDIGO 6 de 7]
        try:
            pag = int(input("Qual o número de páginas desejadas? "))
            if pag <= 20:
                print("Essa quantidade não possui desconto")
                return pag
            elif 20 <= pag < 200:
                desconto = float(pag * 0.85)
                print('Número de páginas com o desconto de 15%')
                return desconto
            elif 200 <= pag < 2000:
                desconto = float(pag * 0.80)
                print('Número de páginas com o desconto de 20%')
                return desconto
            elif 2000 <= pag < 20000:
                desconto = float(pag * 0.75)
                print('Número de páginas com o desconto de 25%')
                return desconto
            else:
                print("Não aceitamos esta quantidade.")
        except ValueError:
            print("Por favor, digite um número válido.")

# [EXIGÊNCIA DE CÓDIGO 4 de 7]
def servico_extra():
    while True:
        # [EXIGÊNCIA DE CÓDIGO 6 de 7]
        try:
            print("1 - Para encadernação simples é cobrado um valor extra de 15 reais")
            print("2 - Para encadernação de capa dura é cobrado um valor extra de 40 reais")
            print("0 - Para não querer nada é cobrado um valor extra de 0 reais")
            serv = int(input("Qual o serviço adicional? "))
            if serv == 1:
                print("Encadernação simples")
                return 15.0
            elif serv == 2:
                print("Encadernação de capa dura")
                return 40.0
            elif serv == 0:
                print("Sem serviço adicional")
                return 0.0
            else:
                print("Não existe esse serviço. Tente novamente.")
        except ValueError:
            print("Por favor, digite um serviço válido.")
            print("Por favor, entre com o número de páginas novamente")

valor_unitario = escolha_servico()
paginas_com_desconto = num_pagina()
valor_adicional = servico_extra()

#[EXIGÊNCIA DE CÓDIGO 5 de 7];
total = valor_adicional + (valor_unitario * paginas_com_desconto)

print(f"Valor total a pagar: R$ {total:.2f} ( servico {valor_unitario:.2f} * páginas: {paginas_com_desconto:.2f} + extra: {valor_adicional}  )")

