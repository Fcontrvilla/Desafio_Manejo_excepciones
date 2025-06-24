
from error import DimensionError

"""3. En el archivo foto.py entregado, modificar los métodos setter de alto y ancho, de forma
tal que se lance una excepción de tipo DimensionError en caso de que el nuevo valor
ingresado no cumpla con las condiciones descritas. En caso contrario, asignar el
nuevo valor al atributo de instancia correspondiente."""

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta  #se agrega self...

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        #si el ancho es mayor a 1 o menor que max
        if ancho>=1 and ancho <= self.Max:
            self.__ancho = ancho
        else:
            raise DimensionError("El ancho no cumple con las condiciones", ancho, Foto.MAX)
            

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto >=1 and alto <= self.MAX:
            self.__alto = alto
        else:
            raise DimensionError("El alto no cumple con las condiciones", alto, Foto.MAX)

        

