"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    prim_num_int = int(input('Informe o primeiro número inteiro: '))
    seg_num_int = int(input('Informe o segundo número inteiro: '))
    num_real = float(input('Informe um número real: '))

    #  o produto do dobro do primeiro com metade do segundo;
    calculo_1 = (prim_num_int * 2) * (seg_num_int / 2)

    #  a soma do triplo do primeiro com o terceiro;
    calculo_2 = (3 * prim_num_int) + num_real

    #  o terceiro elevado ao cubo.
    calculo_3 = num_real ** 3

    print(
        f'O produto do dobro do primeiro com metade do segundo é {calculo_1:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {calculo_2:.2f}')
    print(f'O terceiro elevado ao cubo é {calculo_3:.2f}')


#  calcular_formulas()
