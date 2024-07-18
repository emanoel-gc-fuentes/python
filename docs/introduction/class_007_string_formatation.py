"""
F-Strings (Formatação de Strings) em Python

Definição Técnica:
F-strings, introduzidas no Python 3.6, são uma forma simples e intuitiva de formatar strings. O nome "f-string" vem do prefixo `f` ou `F` que se coloca antes da string. Dentro de uma f-string, expressões entre chaves `{}` são avaliadas em tempo de execução e formatadas usando a especificação padrão de formatação de strings do Python.

Sintaxe:
A sintaxe básica de uma f-string é:
    f"texto {variavel} texto {expressao}"

A string é precedida por `f` ou `F` e expressões Python são incluídas dentro de chaves `{}`.

Exemplos de uso:

1. Interpolação de variáveis:
   nome = "Alice"
   idade = 30
   saudacao = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
   print(saudacao)
   # Saída: Olá, meu nome é Alice e eu tenho 30 anos.

2. Avaliação de expressões:
   a = 5
   b = 10
   resultado = f"A soma de {a} e {b} é {a + b}."
   print(resultado)
   # Saída: A soma de 5 e 10 é 15.

Vantagens das f-strings:
- São mais concisas e legíveis comparadas a outras técnicas de formatação como `%` e `str.format()`.
- Permitem a inclusão de expressões complexas diretamente dentro das chaves.
- Suportam especificadores de formato para controle detalhado da apresentação de valores.

Especificadores de Formato:
Os especificadores de formato podem ser usados para controlar a apresentação de valores dentro das f-strings. Por exemplo:
   valor = 1234.56789
   formatado = f"Valor formatado: {valor:.2f}"
   print(formatado)
   # Saída: Valor formatado: 1234.57

Neste exemplo, `.2f` especifica que o valor deve ser formatado como um número de ponto flutuante com duas casas decimais.

Conclusão:
F-strings são uma ferramenta poderosa e versátil para formatação de strings em Python, proporcionando uma maneira clara e eficiente de incorporar variáveis e expressões dentro de strings.
"""
