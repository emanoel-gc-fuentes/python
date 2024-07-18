"""
Coerção de Dados em Python

Definição:
Coerção de dados é a técnica de converter um valor de um tipo de dado para outro. Isso pode ser necessário para realizar operações que exigem que os operandos sejam do mesmo tipo.

Sintaxe:
A coerção de dados pode ser feita usando funções de conversão embutidas em Python, tais como:
- int()
- float()
- str()
- bool()
"""

# Exemplos de uso:

# 1. Convertendo uma string para inteiro:
string_numero = "123"
inteiro_numero = int(string_numero)
print(inteiro_numero)  # Saída: 123
print(type(inteiro_numero))  # Saída: <class 'int'>

# 2. Convertendo um número para string:
numero = 456
string_numero1 = str(numero)
print(string_numero1)  # Saída: "456"
print(type(string_numero1))  # Saída: <class 'str'>
   
"""
Outros exemplos de coerção de dados incluem:
- Convertendo uma string para float: float("12.34")
- Convertendo um valor booleano para inteiro: int(True)
- Convertendo um número para booleano: bool(0)

Observações:
- A coerção de dados deve ser feita com cuidado para evitar erros de execução, especialmente quando os dados não são adequados para a conversão (por exemplo, tentar converter uma string não numérica para um inteiro).
"""
