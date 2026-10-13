"""Historias de dos líneas; la presentación pertenece exclusivamente a la CLI."""

HISTORIAS = {
    1: (
        "El chef es la CPU y las órdenes son procesos esperando atención.\n"
        "Decidirá por llegada, duración, turnos o prioridad: ¿cuánto esperará cada cliente?"
    ),
    2: (
        """--- MÓDULO 2: CAOS EN LA CAFETERÍA (SINCRONIZACIÓN Y CONCURRENCIA) ---
Bienvenidos a la zona de cafetería durante la hora pico. 

Aquí los Meseros (Productores) toman los pedidos y los dejan en la Barra (Búfer).
Los Baristas (Consumidores) toman esos pedidos de la Barra para preparar los cafés.

Reglas de la casa para evitar un desastre concurrente:
1. Espacio limitado: La Barra tiene una capacidad máxima. Si se llena de tickets, 
   los Meseros deben esperar sin hacer nada (Semáforo de Huecos).
2. Sin pedidos, no hay trabajo: Si la Barra está vacía, los Baristas deben esperar 
   hasta que llegue una orden (Semáforo de Disponibles).
3. Manos quietas: Solo una persona puede poner o quitar un ticket de la Barra 
   a la vez para evitar que se rompan o se dupliquen (Mutex).
4. El cuello de botella: Solo hay UNA máquina de café compartida. Los Baristas 
   tendrán que turnarse para usarla (Lock de Cafetera).

Iniciando la simulación de hilos en tiempo real...\n"""
    ),
    3: (
        "La mesa del chef es la RAM; la despensa es el disco y los ingredientes son páginas.\n"
        "Cuando la mesa se llena, FIFO, LRU u Óptimo eligen qué ingrediente retirar."
    ),
}


def mostrar(modulo):
    print("\n" + HISTORIAS[modulo] + "\n")
