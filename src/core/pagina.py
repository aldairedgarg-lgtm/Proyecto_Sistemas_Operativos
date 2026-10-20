"""Una página lógica; su número no es una dirección física."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Pagina:
    numero: int

    def __post_init__(self):
        if type(self.numero) is not int or self.numero < 0:
            raise ValueError("El número de página debe ser un entero >= 0.")
