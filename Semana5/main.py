from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

# Punto de arranque 
mi_restaurante = Restaurante("Restaurante de mariscos")

plato1 = Producto("Ceviche de pescado", 3.50, True)
plato2 = Producto("Encebollado", 3.00, True)
plato3 = Producto("Arroz de camaron", 4.00, True)

cliente1 = Cliente("Daniel", "0911111111")
cliente2 = Cliente("Wilson", "0922222222")


mi_restaurante.registrar_producto(plato1)
mi_restaurante.registrar_producto(plato2)
mi_restaurante.registrar_producto(plato3)

mi_restaurante.registrar_cliente(cliente1)
mi_restaurante.registrar_cliente(cliente2)


mi_restaurante.crear_pedido(cliente1, plato1)
mi_restaurante.crear_pedido(cliente2, plato2)

# Despliegue de datos 
mi_restaurante.mostrar_informacion()