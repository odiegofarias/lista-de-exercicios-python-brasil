"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_trinagulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_trinagulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_trinagulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_trinagulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_trinagulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_trinagulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_trinagulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""
    """
    Com os três segmentos de reta medindo 5cm, 10cm e 9cm, podemos           formar um triângulo?
    Vamos aplicar a regra da condição de existência de um triângulo          para todos os lados.
    |10 – 9| < 5 < 10 + 9
    1 < 5 <19 (VERDADEIRO)
    
    |9 – 5| < 10 < 9 + 5
    4 < 10 < 14 (VERDADEIRO)
    
    |5 – 10| < 9 < 10 + 5
    5 < 9 < 15 (VERDADEIRO)
  """
    lado_triangulo = True

    if lado_b - lado_c < lado_a < lado_b + lado_c:
        lado_triangulo = True

        if lado_c - lado_a < lado_b < lado_c + lado_a:
            lado_triangulo = True

            if lado_a - lado_b < lado_a < lado_a + lado_b:
                lado_triangulo = True

            else:
                lado_triangulo = False

        else:
            lado_triangulo = False

    else:
        lado_triangulo = False

    if lado_triangulo:
        #  O triângulo equilátero possui todos os lados congruentes, isto é,        #  todos os lados do triângulo possuem a mesma medida.
        if lado_a == lado_b and lado_b == lado_c:
            return 'Triângulo Equilátero'

        #  O triângulo isósceles possui pelo menos dois lados congruentes, ou       #  seja, possui dois lados iguais e um diferente.
        elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
            return 'Triângulo Isósceles'

        #  O triângulo escaleno possui todos os seus lados diferentes, ou seja,     #  cada lado tem uma medida diferente.
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é um triângulo'
