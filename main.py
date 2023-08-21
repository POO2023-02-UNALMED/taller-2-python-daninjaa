class Asiento:
    def __init__(self, color: str, precio: int, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color


class Motor:
    def __init__(self, numeroCilindros: int, tipo: str, registro: int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro: int):
        if isinstance(registro, int):
            self.registro = registro

    def asignarTipo(self, tipo: str):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    CANTIDAD_CREADOS = 0

    def __init__(self, modelo: str, precio: int, asientos: list, marca: str, motor: Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.CANTIDAD_CREADOS += 1

    def cantidadAsientos(self):
        num_asientos = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                num_asientos += 1
        return num_asientos

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento.registro != self.registro:
                return "Las piezas no son originales"
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        else:
            return "Auto original"