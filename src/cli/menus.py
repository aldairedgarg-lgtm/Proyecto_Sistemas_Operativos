"""Entrada híbrida. Aquí viven input(), menús y lectura de JSON."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
ARCHIVOS = {1: "procesos.json", 2: "sincro_config.json", 3: "memoria.json"}


def elegir(titulo, opciones):
    print("\n" + titulo)
    for clave, texto in opciones.items():
        print(f"  {clave}. {texto}")
    while True:
        opcion = input("Seleccione una opción: ").strip().upper()
        if opcion in opciones:
            return opcion
        print("Opción inválida. Intente de nuevo.")


def leer_entero(mensaje, minimo=0, maximo=None):
    while True:
        try:
            numero = int(input(mensaje).strip())
            if numero < minimo or (maximo is not None and numero > maximo):
                raise ValueError
            return numero
        except ValueError:
            rango = f"entre {minimo} y {maximo}" if maximo is not None else f">= {minimo}"
            print(f"Ingrese un número entero {rango}.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto and texto.isprintable() and len(texto) <= 60:
            return texto
        print("Ingrese entre 1 y 60 caracteres imprimibles.")


def principal():
    return elegir("SO-Sim | Restaurante de Sistemas Operativos", {
        "1": "Procesos y planificación", "2": "Sincronización: productor-consumidor",
        "3": "Memoria y paginación", "0": "Salir"})


def menu_procesos():
    return elegir("Módulo 1 | SJF y Prioridad sin expropiación", {
        "1": "FCFS", "2": "SJF", "3": "Round Robin", "4": "Prioridad (1 = mayor)",
        "5": "Comparar los cuatro", "6": "Demostración Linux: fork / execvp / wait",
        "0": "Volver al menú principal"})


def menu_memoria():
    return elegir("Módulo 3 | Reemplazo de páginas", {
        "1": "FIFO", "2": "LRU", "3": "Óptimo", "4": "Comparar los tres",
        "0": "Volver al menú principal"})


def solicitar_datos(modulo):
    """Se llama en CADA entrada a un módulo, nunca elige JSON implícitamente."""
    opcion = elegir(f"Módulo {modulo} | Origen de los datos", {
        "A": f"Cargar datos desde {ARCHIVOS[modulo]}",
        "B": "Ingresar los datos manualmente por consola",
        "0": "Volver al menú principal"})
    if opcion == "0":
        return None
    if opcion == "A":
        with (DATA_DIR / ARCHIVOS[modulo]).open(encoding="utf-8") as archivo:
            return json.load(archivo)
    if modulo == 1:
        cantidad = leer_entero("Cantidad de procesos (1-100): ", 1, 100)
        quantum = leer_entero("Quantum de Round Robin: ", 1)
        procesos = []
        for i in range(1, cantidad + 1):
            print(f"\nProceso P{i}")
            procesos.append({
                "pid": f"P{i}", "nombre": leer_texto("Nombre de la orden: "),
                "llegada": leer_entero("Tiempo de llegada: ", 0),
                "rafaga": leer_entero("Ingrese ráfaga del proceso: ", 1),
                "prioridad": leer_entero("Prioridad (1 = mayor): ", 1),
            })
        return {"quantum": quantum, "procesos": procesos}
    if modulo == 2:
        return {
            "capacidad": leer_entero("Capacidad de la bandeja (1-20): ", 1, 20),
            "productores": leer_entero("Meseros productores (1-8): ", 1, 8),
            "consumidores": leer_entero("Baristas consumidores (1-8): ", 1, 8),
            "pedidos_por_productor": leer_entero("Pedidos por mesero (1-30): ", 1, 30),
            "pausa_ms": leer_entero("Pausa de demostración en ms (0-100): ", 0, 100),
        }
    marcos = leer_entero("Cantidad de marcos (1-20): ", 1, 20)
    while True:
        cadena = input("Ingrese la cadena de páginas separada por comas: ")
        try:
            referencias = [int(parte.strip()) for parte in cadena.split(",")]
            if not 1 <= len(referencias) <= 1000 or any(n < 0 for n in referencias):
                raise ValueError
            return {"marcos": marcos, "referencias": referencias}
        except ValueError:
            print("Ingrese de 1 a 1000 enteros no negativos; ejemplo: 7,0,1,2,0.")
