"""
Função input() em Python

Definição Técnica:
A função `input()` é usada para obter dados do usuário. Quando chamada, ela pausa a execução do programa e espera que o usuário digite algo no console, retornando o valor digitado como uma string.

Sintaxe:
A sintaxe básica da função `input()` é:
    input([prompt])

Onde `prompt` é uma string opcional que pode ser exibida ao usuário para indicar o que ele deve digitar.

Exemplos de uso:

1. Obter uma entrada simples do usuário:
   nome = input("Digite seu nome: ")
   print(f"Olá, {nome}!")
   # Quando executado, o programa exibirá "Digite seu nome: ", esperará o usuário digitar algo e pressionar Enter, então exibirá "Olá, [nome digitado]!".

2. Obter um número do usuário e realizar uma operação:
   idade = input("Digite sua idade: ")
   idade = int(idade)  # Converte a string para um inteiro
   ano_nascimento = 2024 - idade
   print(f"Você nasceu em {ano_nascimento}.")
   # Quando executado, o programa exibirá "Digite sua idade: ", esperará o usuário digitar algo e pressionar Enter, então calculará e exibirá o ano de nascimento.

Observações:
- O valor retornado por `input()` é sempre uma string. Se você espera um número ou outro tipo de dado, deve converter a string usando as funções apropriadas, como `int()` para inteiros ou `float()` para números de ponto flutuante.
- Se o usuário digitar algo que não pode ser convertido para o tipo desejado (por exemplo, letras quando se espera um número), uma exceção será levantada.

Tratamento de Exceções:
Para tornar o programa mais robusto, você pode usar um bloco try-except para lidar com entradas inválidas:
   try:
       idade = int(input("Digite sua idade: "))
       ano_nascimento = 2024 - idade
       print(f"Você nasceu em {ano_nascimento}.")
   except ValueError:
       print("Por favor, digite um número válido.")
   # Este exemplo trata o caso em que o usuário não digita um número válido, exibindo uma mensagem de erro amigável.

Conclusão:
A função `input()` é fundamental para interatividade em programas Python, permitindo que você obtenha dados do usuário e os utilize em seu programa. Com a conversão apropriada e tratamento de exceções, você pode garantir que seu programa lide com entradas de usuário de forma eficaz.
"""
