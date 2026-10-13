"""Historias de dos líneas; la presentación pertenece exclusivamente a la CLI."""

HISTORIAS = {
    1: (
        "El chef es la CPU y las órdenes son procesos esperando atención.\n"
        "Decidirá por llegada, duración, turnos o prioridad: ¿cuánto esperará cada cliente?"
    ),
    2: (
        "Los meseros dejan pedidos en una bandeja limitada y los baristas los recogen.\n"
        "La máquina de café es compartida: un mutex da el turno y los semáforos regulan la bandeja."
    ),
    3: (
        "La mesa del chef es la RAM; la despensa es el disco y los ingredientes son páginas.\n"
        "Cuando la mesa se llena, FIFO, LRU u Óptimo eligen qué ingrediente retirar."
    ),
}


def mostrar(modulo):
    print("\n" + HISTORIAS[modulo] + "\n")
