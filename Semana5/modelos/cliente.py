class Cliente:
    def __init__(self,nombre: str, celular : int):
        #Cliente guarda su nombre y numero
        self.nombre: str = nombre
        self.celular: int = celular

    def __str__(self)-> str:
        return f"Cliente: {self.nombre} , celular: {self.celular}"