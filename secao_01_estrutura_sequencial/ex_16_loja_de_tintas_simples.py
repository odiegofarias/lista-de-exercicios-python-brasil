"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area = float(input('Informe a área em (m²) que deseja pintar: '))
    lata_de_tinta = 80.0
    calc_litros = area / (18 * 3 - 4)
    print(
        f'Você deve comprar {int(calc_litros)} lata(s) tinta ao custo de R$ {calc_litros * 80.0:.2f}')


#  calcular_latas_e_preco_de_tinta()
