import pygame
import random
#grandezze espresse in pixel
LARGHEZZA = 800
ALTEZZA = 600
#Codici rgb
BIANCO = (255, 255, 255)
BLU = (0, 0, 255)
ROSSO = (255, 0, 0)

game_display = pygame.display.set_mode((LARGHEZZA,ALTEZZA))
pygame.display.set_caption('Il mondo di Bob')
clock = pygame.time.Clock()


class Giocatore:
    #Costruttore
    def __init__(self, nome, sesso):
        self.x = random.randrange(0, LARGHEZZA)
        self.y = random.randrange(0, ALTEZZA)
        self.nome = nome
        self.sesso = sesso

    #metodo per mostrare sullo schermo l'immagine dell'istanza
    def mostra(self, screen, immagine):
        screen.blit(immagine, (self.x, self.y))


class Ostacolo:
    #Costruttore
    def __init__(self, numero, pericolosità, movimento):
        self.x = random.randrange(0, LARGHEZZA)
        self.y = random.randrange(0, ALTEZZA)
        self.numero = numero
        self.pericolosità = pericolosità
        self.movimento = movimento


    #metodo per mostrare sullo schermo l'immagine dell'istanza
    def mostra(self, screen, immagine):
        screen.blit(immagine, (self.x, self.y))


    
def start():
    #creo istanza bob ed istanza ostacolo1 appartenenti
    #rispettivamente alle classi Giocatore ed Ostacolo
    bob = Giocatore('Bob', 'M')
    ostacolo1 = Ostacolo(1,5,False)

    #Carico le immagini da attribuire alle istanze
    bob_img = pygame.image.load('bob.png')
    ostacolo1_img = pygame.image.load('ostacolo1.png')
  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #definisco lo sfondo del videogioco del colore bianco
        game_display.fill(BIANCO) 
        #mostro sullo schermo bob e l'ostacolo
        bob.mostra(game_display, bob_img)
        ostacolo1.mostra(game_display, ostacolo1_img)
        
        pygame.display.update()
        #definisco gli fps
        clock.tick(60)


start()