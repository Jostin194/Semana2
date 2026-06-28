class Cliente:

    def __init__(self, nombre: str, celular: str):
        # Identificadores descriptivos 
        self.nombre: str = nombre
        self.celular: str = celular

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} ; Celular: {self.celular}"