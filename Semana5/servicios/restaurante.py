from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
        self.lista_pedidos: list[dict] = []  # Tu lista de diccionarios para pedidos

    def registrar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def crear_pedido(self, cliente: Cliente, producto: Producto) -> None:
    
        pedido: dict = {
            "cliente": cliente,
            "producto": producto
        }
        self.lista_pedidos.append(pedido)

    def mostrar_informacion(self) -> None:
        print(f"\nINFORMACION DEL {self.nombre_restaurante.upper()}")
        print("=" * 50)
        
        print("Platos disponibles:")
        for plat in self.lista_productos:
            print(plat)  
            
        print("\nClientes registrados:")
        for cli in self.lista_clientes:
            print(cli)   
            
        print("\nPedidos de platos:")
        for ped in self.lista_pedidos:
            
            print(f"El cliente {ped['cliente'].nombre} ordenó: {ped['producto'].nombre}")
        print("=" * 50 + "\n")