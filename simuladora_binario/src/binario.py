def decimal_a_binario(n, bits):
    # devuelve lista de bits de longitud 'bits'
    resultado = []
    for i in range(bits):
        print(n % 2)
        resultado.append(n % 2)
        n = n // 2
    # la lista está al revés (LSB primero)
    return resultado  # ej. [1,0,1] para 5 en 3 bits

def binario_a_decimal(bits_list):
    total = 0
    for i in range(len(bits_list)):
        total += bits_list[i] * (2 ** i)
    return total
