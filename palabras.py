import unicodedata

from random import choice

from data.palabras_comunes import palabras_comunes

class Palabras:
    
    def __init__(self):
        self.palabras = palabras_comunes
        self.palabra_secreta = self.seleccionar_palabra()
        self.palabra_secreta_sin_acentos = self.quitar_acentos(self.palabra_secreta)
        self.palabra_oculta = self.crear_palabra_oculta() # palabra oculta es la de los guiones bajos que no se sabe cual es
    
    def quitar_acentos(self, texto):
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join([c for c in texto if unicodedata.category(c) != 'Mn'])
        return unicodedata.normalize('NFC', texto)
   
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
        """
        Normalizamos ambas letras, la secreta y la intentada, para
        compararlas obviando los acentos y otros simbolos raros, y 
        en minuscula
        - Las palabras de mi lista de palabras esta en minuscula
        - La función list() toma un iterable (como una lista) y crea una nueva lista que es una copia de los elementos del iterable original.
        - enumerate(...): Es una función que toma una secuencia (en este caso, self.palabra_secreta) y devuelve un iterable de pares (índice, elemento).
        - i: En cada iteración del bucle, i tomará el valor del índice actual (la posición) de la letra en la palabra_secreta (empezando desde 0)
        """
        letra_intentada_normalizada = self.quitar_acentos(letra_intentada).lower()
        
        # creamos una nueva lista para comparar las letras
        nueva_palabra_oculta = list(self.palabra_oculta)
        for i, letra_secreta in enumerate(self.palabra_secreta):
            letra_secreta_normalizada = self.quitar_acentos(letra_secreta).lower()
            if letra_secreta_normalizada == letra_intentada_normalizada:
                nueva_palabra_oculta[i] = self.palabra_secreta[i]
        # devolvemos la palabra oculta actualizada
        self.palabra_oculta = nueva_palabra_oculta
        print(f"Intento: '{letra_intentada}', Palabra oculta: {self.palabra_oculta}")
        
        return ' '.join(self.palabra_oculta)
    
    def palabra_adivinada(self):
        """
        Comprobamos si la palabra oculta ya no contiene guiones bajos
        """
        return '_' not in self.palabra_oculta
            
    
        

    

