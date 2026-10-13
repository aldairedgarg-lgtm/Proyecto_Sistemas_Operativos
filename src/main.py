"""SO-Sim: ejecutar con python3 -B src/main.py desde SO-Sim-Project.

Python 3.9+ y biblioteca estándar. La opción de syscalls requiere Linux.
El árbol utiliza paquetes de espacio de nombres, sin archivos __init__.py.
"""

import sys

# Evita generar carpetas __pycache__ en el árbol solicitado.
sys.dont_write_bytecode = True

from cli import menus, narrativas, visualizador
from modules.m1_procesos import planificador, syscalls_sim
from modules.m2_sincronizacion import prod_cons
from modules.m3_memoria import paginacion


def ejecutar_modulo_1(datos):
    planificador.validar_datos(datos)
    opciones = {"1": "FCFS", "2": "SJF", "3": "RR", "4": "PRIORIDAD"}
    while True:
        opcion = menus.menu_procesos()
        if opcion == "0":
            return
        if opcion in opciones:
            visualizador.procesos(planificador.simular(datos, opciones[opcion]))
        elif opcion == "5":
            resultados = planificador.comparar(datos)
            for resultado in resultados:
                visualizador.procesos(resultado)
            visualizador.comparar_procesos(resultados)
        elif opcion == "6":
            visualizador.syscalls(syscalls_sim.demostrar())


def ejecutar_modulo_3(datos):
    paginacion.validar_datos(datos)
    opciones = {"1": "FIFO", "2": "LRU", "3": "OPTIMO"}
    while True:
        opcion = menus.menu_memoria()
        if opcion == "0":
            return
        if opcion in opciones:
            visualizador.memoria(paginacion.simular(datos, opciones[opcion]))
        else:
            resultados = paginacion.comparar(datos)
            for resultado in resultados:
                visualizador.memoria(resultado)
            visualizador.comparar_memoria(resultados)


def main():
    try:
        while True:
            opcion = menus.principal()
            if opcion == "0":
                print("Gracias por visitar SO-Sim.")
                return
            modulo = int(opcion)
            try:
                datos = menus.solicitar_datos(modulo)
                if datos is None:
                    continue
                narrativas.mostrar(modulo)
                if modulo == 1:
                    ejecutar_modulo_1(datos)
                elif modulo == 2:
                    visualizador.sincronizacion(prod_cons.ejecutar(datos))
                else:
                    ejecutar_modulo_3(datos)
            except (ValueError, OSError, RuntimeError) as error:
                print(f"\nNo se pudo ejecutar el módulo: {error}")
                print("Revise los datos e ingrese nuevamente al módulo.")
    except (EOFError, KeyboardInterrupt):
        print("\nSesión finalizada.")


if __name__ == "__main__":
    main()
