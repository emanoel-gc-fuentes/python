# Funções em Python

# Definição:
# Funções são blocos de código que são executados quando chamados. 
# Elas podem receber parâmetros (argumentos) e retornar valores ou simplesmente executar um bloco de código quando acionadas.

# Sintaxe:
# def nome_da_funcao(parametro1, parametro2, ...):
#     bloco de código
#     return valor

# Exemplos de Funções

# Função que retorna a soma de dois números (Necessário argumentos).
def somar(x, y):
    """
    Retorna a soma de dois números.
    
    Parâmetros:
    x (int, float): Primeiro número.
    y (int, float): Segundo número.
    
    Retorna:
    int, float: A soma de x e y.
    """
    return x + y

# Função que retorna saudação (Não precisa de argumentos).
def saudacao():
    """
    Retorna uma saudação.
    
    Retorna:
    str: Uma mensagem de saudação.
    """
    return 'Olá, Mundo!'

# # Testando as funções
if __name__ == "__main__":
    # Teste da função somar
    soma = somar(2, 3)
    print(f"A soma de 2 e 3 é: {soma}")  # A soma de 2 e 3 é: 5

    # Teste da função saudacao
    mensagem = saudacao()
    print(f"Mensagem de saudação: {mensagem}")  # Mensagem de saudação: Olá, Mundo!


# É possível referenciar uma função em uma variável. Isso pode ser útil para passar funções como argumentos para outras funções,
# ou para simplificar o código ao reutilizar funções de maneira mais flexível.

# Exemplo de referenciação de função
variavel_saudacao = saudacao

# Chamando a função referenciada
print(variavel_saudacao())  # Saída: Olá, Mundo!

# Função que recebe outra função como argumento
def executar_funcao(func):
    """
    Executa a função passada como argumento.
    
    Parâmetros:
    func (function): Função a ser executada.
    
    Retorna:
    O retorno da função passada como argumento.
    """
    return func()

# Utilizando a função que recebe outra função como argumento
resultado = executar_funcao(saudacao)
print(f"Resultado da execução da função saudacao: {resultado}")  # Saída: Olá, Mundo!

# Parâmetros == Variáveis
# Argumentos == Valores

# def função(parametro_variável):
#     bloco de código

# função(argumento_valor)

