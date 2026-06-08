class Planta:
    def __init__(self, especie, tipo, altura=10):
        self.especie = especie
        self.tipo = tipo
        self.altura = altura  

    def crecer(self):
        """
        Incrementa la altura de la planta.
        """
        self.altura += 5

    def mostrar_informacion(self):
        """
        Muestra la información de la planta.
        """
        print(f"Planta: {self.especie} ({self.tipo})")
        print(f"Altura actual: {self.altura} cm")


# Creación de un objeto con una planta más conocida
mi_planta = Planta("Girasol", "Exterior")

# Uso de un método del objeto (la planta crece)
mi_planta.crecer()

# Mostrar información del objeto
mi_planta.mostrar_informacion()