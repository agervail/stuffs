import pygame

pygame.init()
pygame.mouse.set_visible(False)
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode([320,240])

continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les evenements recus
		if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
			continuer = 0      #On arrete la boucle
