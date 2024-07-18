"""
Operadores em Python

Definição:
Operadores são símbolos que realizam operações em variáveis e valores. Em Python, existem diferentes tipos de operadores, como operadores aritméticos, de comparação, lógicos, de atribuição, entre outros.

Principais tipos de operadores:

1. Operadores Aritméticos:
   - Adição: +
   - Subtração: -
   - Multiplicação: *
   - Divisão: /
   - Divisão inteira: //
   - Módulo: %
   - Exponenciação: **

2. Operadores de Comparação:
   - Igual a: ==
   - Diferente de: !=
   - Maior que: >
   - Menor que: <
   - Maior ou igual a: >=
   - Menor ou igual a: <=

3. Operadores Lógicos:
   - E lógico: and
   - Ou lógico: or
   - Não lógico: not

4. Operadores de Atribuição:
   - Atribuição: =
   - Adição e atribuição: +=
   - Subtração e atribuição: -=
   - Multiplicação e atribuição: *=
   - Divisão e atribuição: /=

Exemplos de uso:

1. Uso de operadores aritméticos:
   x = 10
   y = 3
   soma = x + y
   divisao_inteira = x // y
   print(soma)  # Saída: 13
   print(divisao_inteira)  # Saída: 3

2. Uso de operadores de comparação e lógicos:
   a = 5
   b = 8
   c = (a > b)  # False
   d = (a < b)  # True
   resultado_logico = c or d
   print(c)  # Saída: False
   print(d)  # Saída: True
   print(resultado_logico)  # Saída: True

Nota sobre a Precedência dos Operadores:
A precedência dos operadores define a ordem na qual as operações são realizadas. Em Python, a precedência dos operadores, do mais alto para o mais baixo, é a seguinte:
   1. Operadores de Exponenciação: **
   2. Operadores Aritméticos: *, /, //, %
   3. Operadores Aritméticos: +, -
   4. Operadores de Comparação: ==, !=, >, <, >=, <=
   5. Operadores Lógicos: not, and, or

Você pode usar parênteses para alterar a ordem de avaliação conforme necessário. Por exemplo:
   resultado = (2 + 3) * 4  # Saída: 20, porque a expressão entre parênteses é avaliada primeiro.
"""
