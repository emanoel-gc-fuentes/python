"""
Condicionais em Python

Definição Técnica:
Condicionais são estruturas de controle que permitem executar blocos de código diferentes com base em determinadas condições. Em Python, as principais estruturas condicionais são `if`, `elif` e `else`.

Sintaxe:
A sintaxe básica para os condicionais em Python é:
    if condição:
        bloco_de_codigo
    elif outra_condição:
        outro_bloco_de_codigo
    else:
        bloco_de_codigo_final

O bloco de código associado a cada condição é executado apenas se a condição for verdadeira.

Exemplos de uso:

1. Uso básico de `if`, `elif` e `else`:
   temperatura = 25

    if temperatura > 30:
        print("Está quente!")
    elif temperatura < 15:
        print("Está frio!")
    else:
        print("A temperatura está agradável.")
   # Neste exemplo, o programa verifica a temperatura e imprime uma mensagem correspondente.

2. Condicional aninhada:
   idade = 20
   habilitacao = True

    if idade >= 18:
        if habilitacao:
            print("Você pode dirigir.")
        else:
            print("Você precisa de uma habilitação para dirigir.")
    else:
        print("Você é muito jovem para dirigir.")
   # Neste exemplo, o programa verifica a idade e a situação da habilitação para determinar se a pessoa pode dirigir.

Observações:
- A condição dentro de `if` e `elif` deve ser uma expressão que avalia para `True` ou `False`.
- O bloco de código dentro de cada condicional deve ser indentado com um nível de tabulação ou 4 espaços.
- Você pode ter quantos `elif` forem necessários, mas o `else` é opcional e deve ser usado para capturar todas as condições não especificadas anteriormente.
- Condicionais podem ser aninhadas, o que significa que você pode ter uma estrutura condicional dentro de outra.

Uso de Operadores Lógicos e de Comparação:
- Você pode combinar múltiplas condições usando operadores lógicos como `and`, `or`, e `not`.
- Exemplo:
   idade = 22
   tem_carteira = True

    if idade >= 18 and tem_carteira:
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir.")
   # Neste exemplo, ambas as condições (idade e carteira de motorista) devem ser verdadeiras para que a pessoa possa dirigir.

Conclusão:
Condicionais são essenciais para o controle de fluxo em um programa. Eles permitem que seu código tome decisões e execute diferentes blocos de código com base em condições específicas.
"""
