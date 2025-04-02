from random import choice

from data.palabras_comunes import palabras_comunes

class Palabras:
    
    def __init__(self):
        self.palabras = palabras_comunes
        self.palabra_secreta = self.seleccionar_palabra()
        self.palabra_oculta = self.crear_palabra_oculta()

    # elijo una palabra al azar de mi lista
    def seleccionar_palabra(self):
       self.palabra_secreta = choice(palabras_comunes)
       return self.palabra_secreta # devuelve la palabra secreta en su forma original
       
    # creo la palabra oculta con guiones para el jugador
    def crear_palabra_oculta(self):
        self.palabra_oculta = ['_' for _ in self.palabra_secreta]
        return ' '.join(self.palabra_oculta)
        # devuelve una lista con guiones bajos con la misma
        # cantidad de letras que mi palabra secreta y 
        # separada por espacios para el juego

    

