def mdc_estendido(a, b):
    """
    Implementação do MDC estendido de Euclides.
    
    Argumentos:
    - a: número inteiro
    - b: número inteiro
    
    Retorna:
    - O valor do mdc(a,b) e os coeficientes lineares x e y tal que a*x + b*y = mdc(a,b).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        mdc, x, y = mdc_estendido(b % a, a)
        return (mdc, y - (b // a) * x, x)

# Exemplo de uso
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
mdc, x, y = mdc_estendido(a,b)
print(f"Equação: {a} * {x} + {b} * {y} = {mdc}")
