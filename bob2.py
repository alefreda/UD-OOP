import pygame
import random

#grandezze espresse in pixel
LARGHEZZA = 800
ALTEZZA = 600
#Codici rgb
BIANCO = (255, 255, 255)
BLU = (0, 0, 255)
ROSSO = (255, 0, 0)
#impostazioni di gioco (schermo e clock)
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


    def muovi(self):
        #nella variabile key_input memorizza il pulsante premuto
        key_input = pygame.key.get_pressed()  
        #sposta l'istanza di 5 pixel
        if key_input[pygame.K_LEFT]:
            self.x -= 5
        if key_input[pygame.K_UP]:
            self.y -= 5
        if key_input[pygame.K_RIGHT]:
            self.x += 5
        if key_input[pygame.K_DOWN]:
            self.y += 5

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
    
    def muovi(self):
        if self.movimento:
            #movimento random da -4 a 4 pixel
            self.x += random.randrange(-4,5)
            self.y += random.randrange(-4,5)

            #controllo per evitare che si muovano oltre i bordi
            if self.x < 0: self.x = 0
            elif self.x > LARGHEZZA: self.x = LARGHEZZA
        
            if self.y < 0: self.y = 0
            elif self.y > ALTEZZA: self.y = ALTEZZA
        else:
            print("L'ostacolo non si può muovere")
    
    #metodo per mostrare sullo schermo l'immagine dell'istanza
    def mostra(self, screen, immagine):
        screen.blit(immagine, (self.x, self.y))


    
def start():
    #creo istanza bob ed istanze ostacolo appartenenti
    #rispettivamente alle classi Giocatore ed Ostacolo
    bob = Giocatore('Bob', 'M')
    lista_ostacoli = []
    for i in range(20):
        lista_ostacoli.append(Ostacolo(i,10,True))

    #Carico le immagini da attribuire alle istanze
    bob_img = pygame.image.load('bob.png')
    ostacolo1_img = pygame.image.load('ostacolo1.png')
    #definisco il font per il testo 
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #definisco lo sfondo del videogioco del colore bianco
        game_display.fill(BIANCO) 
        #mostro sullo schermo bob e l'ostacolo
        bob.mostra(game_display, bob_img)
        #mostro sulla mappa tutti gli ostacoli e li metto in movimento
        for i in lista_ostacoli:
            i.mostra(game_display, ostacolo1_img)
            i.muovi()
        #richiamo il metodo muovi della classe Giocatore per muovere bob
        bob.muovi()
        #variabili che memorizzano le coordinate di bob
        posizioneBob_x = bob.x
        posizioneBob_y = bob.y
        #mostro sulla schermo le coordinate di Bob
        textsurface = myfont.render(f'Bob si trova nelle coordinate: x: {str(posizioneBob_x)} y: {str(posizioneBob_y)}',False, (0, 0, 0))
        #posiziono e mostro il testo nella mappa
        game_display.blit(textsurface,(450,550))
        pygame.display.flip()
        #pygame.display.update()
        #definisco gli fps
        clock.tick(60)
        
start()
