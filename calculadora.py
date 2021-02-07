
def calcular():

    operation = input('''
    Por favor escolha o tipo de operação:
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    ''')

    # colocar o int atrás do input para validar se o valor inserido é um número
    numero1 = int(input('Coloque o Primeiro Número: '))
    numero2 = int(input('Coloque o Segundo Número: '))

    if operation == '+' :
        #adição
        print('{} + {} = '.format(numero1, numero2))
        print(numero1 + numero2)
    elif operation == '-' :
        #subtração
        print('{} - {} = '.format(numero1, numero2))
        print(numero1 - numero2)
    elif operation == '*':
        #multiplicação
        print('{} * {} = '.format(numero1, numero2))
        print(numero1 * numero2)
    elif operation == '/' :
        #divisão
        print('{} * {} = '.format(numero1, numero2))
        print(numero1 / numero2)
    #divisão
        print('{} + {} = '.format(numero1, numero2))
        print(numero1 / numero2)
    else :
        print('Você não colocou um operador válido, inicie o programa novamente !')


def novamente():
    calcularnovamente = input('''Você gostaria de calcular novamente? Pressione S para SIM ou N para NÃO.: \n''')
    
    if calcularnovamente == 'S':
        calcular()
    elif calcularnovamente == 'N':
        print('Vejo você depois :)')
    else:
        novamente()

calcular()
novamente()

