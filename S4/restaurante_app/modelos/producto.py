class Producto:
    def __init__(self,nombre, precio):
        #El producto guarda su nombre y precio
        self.nombre = nombre
        self.precio = precio
       
    def __str__(self):
        return f"Producto: {self.nombre} , Precio: {self.precio}"