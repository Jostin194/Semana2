# Sistema de Gestión de Restaurante

**Nombre:** Jostin Steeven Villalta Coello

## Descripción del Sistema Desarrollado

Solución basada en el diseño de un sistema básico de gestión de restaurante utilizando los principios de la Programación Orientada a Objetos (POO) e. El sistema evidencia la transición hacia el diseño modular, la abstracción y la correcta segmentación de responsabilidades mediante la comunicación de múltiples archivos e importaciones, prescindiendo de menús interactivos complejos para centrarse en la lógica estructural.

* **Estructura:** Desarrollado dentro de la carpeta principal `restaurante_app`
`modelos`, `servicios` y el archivo de arranque `main.py`.

* **Componentes de los Modelos:** * **Clase Producto (`producto.py`):** Conformada por los atributos `nombre` y `precio`.
 * **Clase Cliente (`cliente.py`):** Conformada por los atributos `nombre` y `celular`.

* **Componentes del Servicio (`restaurante.py`):** Clase `Restaurante` encargada de centralizar la lógica del negocio. Administra el almacenamiento interno mediante listas y provee los métodos encargados de registrar productos, registrar clientes y pedidos.

* **Ejecución:** El archivo de control `main.py` actúa como punto de entrada. Se encarga de importar los módulos correspondientes, instanciar los objetos independientes con sus respectivos atributos, agregarlos al servicio principal y ejecutar los métodos necesarios para mostar la información de manera organizada.


## Reflexión

### Importancia de Modularizar el Software y Separar Responsabilidades

* **Estructura y Organización:** Permite fragmentar un sistema complejo en archivos independientes. Al separar los datos (`modelos/`) de la lógica (`servicios/`), el código es más limpio, ordenado y fácil de comprender.
* **Mantenimiento y Depuración:** Al asignar una sola tarea a cada clase se aíslan los errores. Si falla un cliente o producto, se corrige su archivo específico sin alterar ni romper el resto del sistema.
* **Escalabilidad y Reutilización:** Evita los scripts largos e inmanejables. Crea bloques de construcción independientes que permiten añadir nuevas funciones al restaurante a futuro de forma rápida.
* **Uso de Convenciones Normalizadas:** La aplicación de `PascalCase` para clases (`Producto`, `Cliente`) y `snake_case` para variables/métodos (`lista_productos`, `crear_pedido`) cumple el estándar PEP 8. Los identificadores descriptivos eliminan la ambigüedad y vuelven al software autodocumentado.
* **Coherencia en Tipos de Datos:** Las anotaciones de tipo garantizan la integridad del sistema. Se usa `float` para el precio por precisión decimal; `bool` en la disponibilidad para optimizar el control de la cocina; y `str` para el celular para evitar la pérdida de ceros a la izquierda. Finalmente, las **listas** (datos compuestos) agrupan y relacionan los objetos dinámicamente en memoria, simulando un entorno real.
