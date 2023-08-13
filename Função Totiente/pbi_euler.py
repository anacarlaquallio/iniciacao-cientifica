def euler_totient(n):
    """
    Implementação da função totiente de Euler.
    
    Argumentos:
    - n: número inteiro
    
    Retorna:
    - O valor da função totiente de Euler para o número n.
    """
    result = n  # Inicializa o resultado com n
    
    # Verifica a divisibilidade por todos os números primos até a raiz quadrada de n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result = result * (1 - 1/p)
        p += 1

    # Se n é maior que 1, então há fatores primos
    if n != 1:
        result = result * (1 - 1/(n))
    
    return int(result)

n = int(input("Digite um valor para cálcular a função totiente de n: "))
print(euler_totient(n))