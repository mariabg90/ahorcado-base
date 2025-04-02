from hangman import utils
from hangman.constants import WINDOW_H, WINDOW_W

class Jugador:
    """
    - Creamos un atributo llamado letras_intentadas
    - Lo inicializamos como un set vacío. 
        - set(): es una colección que no permite elementos duplicados, lo cual es perfecto para llevar un registro de las letras que el jugador ya ha probado.

        - letra.isalpha(): Si la entrada es una letra del alfabeto.
    """

    def __init__(self):
        self.letras_intentadas = set() # conjunto de letras intentadas
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.ganado = True

    def intentar_letra(self, letra, palabra_secreta):
        """
        Devuelve True o False
        1. Convertimos la letra introducida en minuscula
            - TODO: que ignore tildes y dieresis (creo que ya lo hace con lo de ascii)
        2. Comprobamos is ya se ha intentado esa letra ys e anade al conjunto de letras intentadas
        3. Comprobamos si la letra introducida esta en la palabra secreta
        4. Si la letra esta en la palabra secreta se anade al conjunto de letras correctas
        5. Si no, se anade al conjuto de letras incorrectas
        """
        letra = letra.lower()
        if letra not in self.letras_intentadas and letra.isalpha():
            # no ha intentado esa letra, se anade a la lista de letras intentadas
            self.letras_intentadas.add(letra)
            if letra in palabra_secreta:
                self.letras_correctas.add(letra)
                return True # devuelve True si la letra es correcta
            else: 
                self.letras_incorrectas.add(letra)
        return False # ya ha intentado la letra

    def obtener_letras_correctas(self):
        return self.letras_correctas

    def obtener_letras_incorrectas(self):
        return self.letras_incorrectas
       
    def mostrar_resultado(self, display, font):
            win_text = font.render("¡Has Ganado!", True, (0, 255, 0))
            win_rect = win_text.get_rect(center=(WINDOW_W // 2, WINDOW_H // 2))
            display.blit(win_text, win_rect)