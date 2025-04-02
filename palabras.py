from random import choice

from data.palabras_comunes import palabras_comunes

class Palabras:
    
    def __init__(self):
        self.palabras = palabras_comunes
        self.palabra_secreta = self.seleccionar_palabra()
        self.palabra_oculta = self.crear_palabra_oculta()

    # elijo una palabra al azar de mi lista
    def seleccionar_palabra(self):
       """
       Devuelve la palabra secreta en su forma original
       """
       self.palabra_secreta = choice(self.palabras)
       return self.palabra_secreta 
       
    # creo la palabra oculta con guiones para el jugador
    def crear_palabra_oculta(self):
        """
        Devuelve una lista con guiones bajos con la misma
        cantidad de letras que mi palabra secreta
        """
        self.palabra_oculta = ['_' for _ in self.palabra_secreta]
        return self.palabra_oculta
        
    def crear_palabra_oculta_formateada(self):
        """
        Lista de guiones bajos separados por espacios para el juego y mostrarla al jugador
        Esta es una funcion puramente visual, es dificil saber
        cuantas letras tiene la palabra si se muestra "______"
        """
        self.palabra_oculta_formateada = ' '.join(self.palabra_oculta)
        return self.palabra_oculta_formateada


    def actualizar_palabra_oculta(self, letra_intentada):
        letra_intentada = letra_intentada.lower() # las palabras de la lista estan en minuscula
        for i, letra_secreta in enumerate(self.palabra_secreta):
            if letra_secreta == letra_intentada:
                self.palabra_oculta[i] = letra_intentada
        # devolvemos la palabra oculta actualizada
        return self.palabra_oculta
    
    def palabra_adivinada(self):
        """
        Comprobamos si la palabra oculta ya no contiene guiones bajos
        """
        if '_' not in self.palabra_oculta:
            return True # la palabra ha sido adivinada
    
        

    

