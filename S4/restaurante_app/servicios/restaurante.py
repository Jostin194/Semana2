from modelos.producto import Producto
from modelos.cliente import Cliente_clase

class Restaurante_clase:
    def __init__(self,nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []
        self.lista_clientes = []
        self.lista_pedidos = []
        
    def registrar_producto(self, producto):
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def crear_pedido(self, cliente, producto):
        pedido = {
            "cliente": cliente,
            "producto": producto
        }
        self.lista_pedidos.append(pedido)

    def mostrar_informacion(self):
        print(f"Informacion del {self.nombre_restaurante.upper()}")
        
        print("Platos disponibles:")
        for plat in self.lista_productos:
            print(plat) 

        print("Clientes resgistrados:")
        for cli in self.lista_clientes:
            print(cli) 

        print("Pedidos de platos:")
        for ped in self.lista_pedidos:
            print(f"El cliente {ped['cliente'].nombre} ordeno: {ped['producto'].nombre}")
        
         
    
    




