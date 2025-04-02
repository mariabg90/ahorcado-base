class Jugador:
    """
    - Creamos un atributo llamado letras_intentadas
    - Lo inicializamos como un set vacío. 
        - set(): es una colección que no permite elementos duplicados, lo cual es perfecto para llevar un registro de las letras que el jugador ya ha probado.

        - letra.isalpha(): Si la entrada es una letra del alfabeto.
    """

    def __init__(self):
        self.letras_intentadas = set() # conjunto de letras intentadas

    def intentar_letra(self, letra):
        letra = letra.lower()
        if letra not in self.letras_intentadas and letra.isalpha():
            self.letras_intentadas.add(letra)
            return True # no ha intentado esa letra, se anade a la lista de letras intentadas
        return False # ya ha intentado la letra

