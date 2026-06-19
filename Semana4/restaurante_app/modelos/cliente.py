class Cliente_clase:
    def __init__(self,nombre, celular):
        #Cliente guarda su nombre y numero
        self.nombre = nombre
        self.celular = celular

    def __str__(self):
        return f"Cliente: {self.nombre} , celular: {self.celular}"
        