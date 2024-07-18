"""
Operadores in e not in em Python

Definição Técnica:
Os operadores `in` e `not in` são usados para verificar a presença de um elemento em uma sequência (como listas, tuplas, strings, dicionários, etc.). O operador `in` retorna `True` se o elemento estiver presente na sequência, enquanto o operador `not in` retorna `True` se o elemento não estiver presente.

Sintaxe:
A sintaxe básica dos operadores `in` e `not in` é:
    elemento in sequencia
    elemento not in sequencia

Exemplos de uso:

1. Verificando a presença de um elemento em uma lista:
   frutas = ["maçã", "banana", "laranja"]

   if "banana" in frutas:
       print("A banana está na lista de frutas.")
   else:
       print("A banana não está na lista de frutas.")
   
   # Saída: A banana está na lista de frutas.

2. Verificando a ausência de um caractere em uma string:
   mensagem = "Olá, mundo!"

   if "x" not in mensagem:
       print("A letra 'x' não está na mensagem.")
   else:
       print("A letra 'x' está na mensagem.")
   
   # Saída: A letra 'x' não está na mensagem.

Observações:
- O operador `in` pode ser usado com qualquer tipo de sequência, incluindo listas, tuplas, strings, dicionários e conjuntos.
- Ao usar `in` com dicionários, ele verifica se a chave está presente, não os valores.
- Os operadores `in` e `not in` são úteis para simplificar a lógica do programa, evitando a necessidade de loops explícitos para verificar a presença de elementos.

Mais exemplos:

3. Verificando a presença de uma chave em um dicionário:
   estudante = {"nome": "Alice", "idade": 21, "curso": "Engenharia"}

   if "idade" in estudante:
       print("A chave 'idade' está presente no dicionário.")
   else:
       print("A chave 'idade' não está presente no dicionário.")
   
   # Saída: A chave 'idade' está presente no dicionário.

4. Verificando a ausência de um elemento em uma tupla:
   numeros = (1, 2, 3, 4, 5)

   if 6 not in numeros:
       print("O número 6 não está presente na tupla.")
   else:
       print("O número 6 está presente na tupla.")
   
   # Saída: O número 6 não está presente na tupla.

Conclusão:
Os operadores `in` e `not in` são ferramentas poderosas e concisas para verificar a presença ou ausência de elementos em sequências. Eles ajudam a tornar o código mais legível e fácil de entender, evitando a necessidade de loops complexos para realizar essas verificações.
"""
