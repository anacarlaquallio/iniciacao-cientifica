def mdc_r(a: int, b: int):
    """
    Implementação recursiva do MDC considerando mdc(a,b) = mdc(b, a%b).
    
    Argumentos:
    - a: número inteiro
    - b: número inteiro
    
    Retorna:
    - O valor do mdc(a,b).
    """
    if (b == 0): return a
    return mdc_r(b, a % b)

def mdc_i(a: int, b: int):
    """
    Implementação iterativa do MDC.
    
    Argumentos:
    - a: número inteiro
    - b: número inteiro
    
    Retorna:
    - O valor do mdc(a,b).
    """
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
print("MDC recursivo: ", mdc_r(a,b))
print("MDC iterativo: ", mdc_i(a,b))

