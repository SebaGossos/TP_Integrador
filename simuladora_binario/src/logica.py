def and_gate(a, b):
    # a y b son 0 o 1
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def or_gate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def xor_gate(a, b):
    # true si son distintos
    if a != b:
        return 1
    else:
        return 0

def not_gate(a):
    if a == 0:
        return 1
    else:
        return 0

def medio_sumador(a, b):
    suma = xor_gate(a, b)
    acarreo = and_gate(a, b)
    return [suma, acarreo]  

def sumador_completo(a, b, c_in):
    s1, c1 = medio_sumador(a, b)
    s2, c2 = medio_sumador(s1, c_in)
    # el acarreo de salida es OR de los dos acarreo parciales
    c_out = or_gate(c1, c2)
    return [s2, c_out]
