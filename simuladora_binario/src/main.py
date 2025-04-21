# from logica import sumador_completo
from binario import decimal_a_binario, binario_a_decimal
from logica import sumador_completo

def sumar_n_bits(a_dec, b_dec, bits=4):
    a_bits = decimal_a_binario(a_dec, bits)
    b_bits = decimal_a_binario(b_dec, bits)
    resultado = []
    c_in = 0
    # iterar cada posición
    for i in range(bits):
        suma_bit, c_in = sumador_completo(a_bits[i], b_bits[i], c_in)
        resultado.append(suma_bit)
    # añadir acarreo final
    resultado.append(c_in)
    # convertir a decimal para mostrar
    return binario_a_decimal(resultado), resultado

if __name__ == "__main__":
    x = int(input("Ingrese primer número: "))
    y = int(input("Ingrese segundo número: "))
    suma_dec, suma_bits = sumar_n_bits(x, y, bits=4)
    print(f"Suma en decimal: {suma_dec}")
    print(f"Suma en binario (LSB→MSB): {suma_bits}")
