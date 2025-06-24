

class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo


    """En la misma clase anterior, sobrecargar el método __str__, de forma tal que si sólo
se ha ingresado mensaje al crear la excepción, se retorna el método de la clase padre.
En caso contrario, crear y retornar un mensaje de retorno utilizando los atributos
mensaje y/o dimension y/o maximo."""
    
    def __str__(self)     #sobrecarga metodo

        if self.dimesion is None and self.maximo is None:
            return super().__str__(Exception)
        
        else:
            return f"se ingresó {self.mensaje}, {self.dimension}, {self.maximo}"