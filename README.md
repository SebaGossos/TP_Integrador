# TP\_Integrador

## 💡 Simulador de Sumador Binario con Puertas Lógicas

Este proyecto implementa en Python un **simulador de sumadores binarios** que utiliza puertas lógicas básicas para demostrar el funcionamiento interno de un sistema de suma binaria paso a paso.

---

## 📘 Descripción

Desarrollamos un simulador educativo que permite modelar y operar:

* Puertas lógicas básicas: `AND`, `OR`, `XOR`, `NOT`
* Medio-sumador (*half adder*)
* Sumador completo (*full adder*)
* Suma de dos números binarios de *n* bits, bit por bit con acarreo
* Generación de **tablas de verdad** para funciones booleanas de *n* entradas

Todo el código fue desarrollado con conceptos básicos de programación estructurada, sin librerías externas:

* **Estructuras secuenciales y condicionales**
* **Bucles**
* **Funciones**
* **Estructuras de datos** (listas, tuplas, diccionarios)

---

## 📂 Estructura del Proyecto

```plaintext
TP_Integrador/
├── src/
│   ├── logica.py       # Definición de puertas lógicas y sumadores
│   ├── binario.py      # Conversión decimal ↔ binario y funciones auxiliares
│   └── main.py         # Programa principal, interacción con el usuario
└── README.md           # Este documento
```

---

## 🧪 Ejecución

1. Cloná el repositorio:

```bash
git clone https://github.com/SebaGossos/TP_Integrador.git
cd TP_Integrador
```

2. (Opcional) Crear un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Ejecutar el programa:

```bash
python src/main.py
```

### 💻 Ejemplo de uso:

```plaintext
Ingrese primer número: 13
Ingrese segundo número: 7
Suma en decimal: 20
Suma en binario (LSB→MSB): [0, 0, 1, 0, 1]
```

---

## 🧮 Generación de Tablas de Verdad

Incluimos una función para generar la tabla de verdad de cualquier función booleana:

```python
from binario import decimal_a_binario

def generar_tabla_verdad(funcion, n_entradas):
    tabla = {}
    for i in range(2 ** n_entradas):
        bits = decimal_a_binario(i, n_entradas)
        tabla[tuple(bits)] = funcion(*bits)
    return tabla
```

---

## 📄 Documentación y Recursos

* 📘 Documentación del proyecto:
  [Google Docs](https://docs.google.com/document/d/1Iin5peslKSUow_U5qhhqIu6ZrIlZw7AVf-Vki0m72UA/edit?usp=sharing)

* 📺 Video explicativo (grupo):
  [YouTube](https://youtu.be/jAtkEcPUYUU/)

---

## 🤖 Evidencia del Uso de IA

Incluimos capturas de pantalla en el repositorio que muestran el uso de ChatGPT para:

* Optimizar funciones (`sumador_completo`, etc.)
* Mejorar claridad de código y nombres de funciones
* Documentar estructuras de datos y lógica

Ejemplo de commit:

```
commit abc123: uso de ChatGPT para refactorizar funciones de suma y documentar código
```

---
