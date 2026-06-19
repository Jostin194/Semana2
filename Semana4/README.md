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

* **Estructura y Organización:** El diseño modular permite fragmentar un sistema complejo en componentes o archivos independientes más pequeños. Al separar los modelos de datos (`modelos/`) y (`servicios/`), el código se vuelve mas facil de complender, limpio y ordenado.

* **Mantenimiento y Depuración:** Al asignar una sola tarea a cada clase, se facilita el mantenimineto de errores. Si falla algo en los clientes o en los productos, se modificaria solo el archivo específico sin romper el resto del codigo.
* **Escalabilidad y Reutilización:** Un único script largo se vuelve imposible de manejar al crecer. La modularidad en POO crea bloques de construcción independientes, permitiendo añadir nuevas funciones para mejorrar el sistema de restaurante a futuro de forma rápida y ordenada.