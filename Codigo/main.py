import sys
import pygame
import player

pygame.init()

size = 1280, 720 
icon = pygame.image.load('..\Arte\Grafico\Icon\icono.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bolim')
pygame.display.set_icon(icon)
Black = (0, 0, 0)
White = (255, 255, 255)


def main():
	clock = pygame.time.Clock()
	quit = False
	full_screen = False
	music = True
	power = open('..\Data\power.txt', 'r')
	P1 = player.P1((625, 315))
	P2 = player.P2((625, 255))
	pygame.mixer.music.load('..\Arte\Audio\Feelings-8-bit.wav')
	pygame.mixer.music.play(100000)
	pygame.mixer.music.set_volume(0.5)
	

	while quit != True:

		#Funciones de la ventana
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:	
					full_screen = not full_screen

					if full_screen:
						pygame.display.set_mode((size), pygame.FULLSCREEN)
					else:
						pygame.display.set_mode((size), 0)

				if event.key == pygame.K_p:

					if music == True:
						pygame.mixer.music.pause()
						music = False
					else:
						pygame.mixer.music.unpause()
						music = True

				if event.key == pygame.K_UP:
					volume = pygame.mixer.music.get_volume()
					pygame.mixer.music.set_volume(volume + 0.1)
					#print(volume)

				if event.key == pygame.K_DOWN:
					volume = pygame.mixer.music.get_volume()
					pygame.mixer.music.set_volume(volume - 0.1)
					#print(volume)

	


		screen.fill(White)
		P1.handle_event(event)
		P2.handle_event(event)
		screen.blit(P1.image, P1.rect)
		screen.blit(P2.image, P2.rect)
		pygame.display.update()
		clock.tick(20)
main()
pygame.quit()