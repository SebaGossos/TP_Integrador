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

def generar_tabla_verdad(funcion, n_entradas):
    tabla = {}
    for i in range(2 ** n_entradas):
        bits = decimal_a_binario(i, n_entradas)
        tabla[tuple(bits)] = funcion(*bits)
    return tabla

def generar_tabla_verdad_operaciones():
    print("Seleccione una operación lógica:")
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. NOT (solo para una entrada)")
    
    opcion = int(input("Ingrese el número de la operación: "))
    
    if opcion == 1:
        operacion = lambda A, B: A and B
        n_entradas = 2
    elif opcion == 2:
        operacion = lambda A, B: A or B
        n_entradas = 2
    elif opcion == 3:
        operacion = lambda A, B: A ^ B
        n_entradas = 2
    elif opcion == 4:
        operacion = lambda A: not A
        n_entradas = 1
    else:
        print("Opción no válida.")
        return

    # Generar tabla de verdad
    tabla = generar_tabla_verdad(operacion, n_entradas)
    
    # Mostrar tabla de verdad
    print("\nTabla de Verdad:")
    for entradas, salida in tabla.items():
        print(f"{entradas} -> {salida}")

if __name__ == "__main__":
    print("Bienvenido al generador de tablas de verdad.")
    generar_tabla_verdad_operaciones()

    x = int(input("Ingrese primer número: "))
    y = int(input("Ingrese segundo número: "))
    suma_dec, suma_bits = sumar_n_bits(x, y, bits=4)
    
    print(f"Suma en decimal: {suma_dec}")
    # Indica que la representación binaria del resultado se muestra desde el bit menos significativo (LSB) al más significativo (MSB).
    print(f"Suma en binario (LSB→MSB): {suma_bits}")