# TP_Integrador
# Simulador de Sumador Binario con Puertas Lógicas

## Descripción

Nosotros hemos desarrollado un simulador en Python que permite modelar y operar sumadores binarios utilizando puertas lógicas básicas. El proyecto muestra paso a paso el funcionamiento de:

- Puertas lógicas: `AND`, `OR`, `XOR`, `NOT`
- Medio-sumador (half adder)
- Sumador completo (full adder)
- Suma de dos números binarios de _n_ bits, mostrando cada bit de resultado y el acarreo final
- Generación de tablas de verdad para cualquier función booleana de _n_ entradas

El código está diseñado con:
- **Estructuras secuenciales**
- **Estructuras condicionales**
- **Estructuras repetitivas**
- **Funciones**
- **Datos complejos** (listas, tuplas, diccionarios)

De esta forma, usamos únicamente los conceptos de programación aprendidos hasta el momento, sin dependencias externas.

## Estructura del proyecto

```plaintext
simulador_binario/
├── src/
│   ├── logica.py       # Definición de puertas y sumadores
│   ├── binario.py      # Conversión decimal ↔ binario y utilidades
│   └── main.py         # Orquestador: lectura de datos y salida de resultados
└── README.md           # Este documento
```

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/simulador_binario.git
   cd simulador_binario
   ```
2. **Crear entorno virtual (opcional)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Uso

1. Ejecutar el programa principal:
   ```bash
   python src/main.py
   ```
2. Ingresar los dos números decimales cuando se soliciten.
3. Observar la salida:
   - Suma en decimal
   - Lista de bits de resultado (LSB → MSB) con el acarreo final.

### Ejemplo

```plaintext
Ingrese primer número: 13
Ingrese segundo número: 7
Suma en decimal: 20
Suma en binario (LSB→MSB): [0, 0, 1, 0, 1]
``` 

## Generación de tablas de verdad

Para generar la tabla de verdad de cualquier función booleana, podemos usar la función `generar_tabla_verdad(funcion, n_entradas)`:

```python
from binario import decimal_a_binario

def generar_tabla_verdad(funcion, n_entradas):
    tabla = {}
    for i in range(2 ** n_entradas):
        bits = decimal_a_binario(i, n_entradas)
        tabla[tuple(bits)] = funcion(*bits)
    return tabla
```

## Evidencia del Uso de IA

Incluimos en el repositorio capturas de pantalla de nuestras interacciones con ChatGPT, donde:

- Optimizamos la función `sumador_completo` usando condicionales y bucles más claros.
- Refinamos nombres de funciones y docstrings.
- Documentamos cada iteración de la IA en mensajes de commit en Git.

Ejemplo de mensaje de commit:
```
commit abc123: usó ChatGPT para mejorar sumador_completo y documentar estructura de datos compleja
```

## Contribuciones

Nosotros agradecemos aportes y sugerencias. Para contribuir:
1. Hacer _fork_ del proyecto.
2. Crear una rama con la mejora (`feature/nueva-puerta`).
3. Hacer _pull request_ describiendo los cambios.
