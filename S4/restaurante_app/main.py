
from servicios.restaurante import Restaurante_clase
from modelos.producto import Producto
from modelos.cliente import Cliente_clase


mi_restaurante = Restaurante_clase("Restaurante de mariscos")


plato1 = Producto("Ceviche de pescado", 3)
plato2 = Producto("Encebollado", 3)
plato3 = Producto("Arroz de camaron", 4)

cliente1 = Cliente_clase("Daniel", "0911111111")
cliente2 = Cliente_clase("Wilson", "0922222222")

mi_restaurante.registrar_producto(plato1)
mi_restaurante.registrar_producto(plato2)
mi_restaurante.registrar_producto(plato3)

mi_restaurante.registrar_cliente(cliente1)
mi_restaurante.registrar_cliente(cliente2)

mi_restaurante.crear_pedido(cliente1, plato1)
mi_restaurante.crear_pedido(cliente2, plato2)

mi_restaurante.mostrar_informacion()