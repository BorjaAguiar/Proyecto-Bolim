import sys
import pygame
import pyglet.clock
import player

pygame.init()

size = 1280, 720 
icon = pygame.image.load('..\Arte\Grafico\Icon\icono.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bolim')
pygame.display.set_icon(icon)

#fps = 0
Black = (0, 0, 0)
White = (255, 255, 255)


def main():
	#reloj = pyglet.clock.Clock()
	#reloj.set_fps_limit(fps)
	clock = pygame.time.Clock()
	quit = False
	full_screen = False
	music = True
	viruses = pygame.image.load('..\Arte\Grafico\Icon\icono.png')
	power = open('..\Data\power.txt', 'r')
	P1 = player.P1((625, 315))
	pygame.mixer.music.load('..\Arte\Audio\Feelings-8-bit.wav')
	pygame.mixer.music.play(100000)
	pygame.mixer.music.set_volume(0.5)
	

	while quit != True:

		#Funciones de la ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit = True

			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:	
					full_screen = not full_screen

					if full_screen:
						pygame.display.set_mode((size), pygame.FULLSCREEN)

					else:
						pygame.display.set_mode((size), 0)

				if evento.key == pygame.K_p:
					if music == True:
						pygame.mixer.music.pause()
						music = False
					else:
						pygame.mixer.music.unpause()
						music = True

				if evento.key == pygame.K_KP_PLUS:
					volume = pygame.mixer.music.get_volume()
					pygame.mixer.music.set_volume(volume + 0.1)
					#print(volume)

				if evento.key == pygame.K_KP_MINUS:
					volume = pygame.mixer.music.get_volume()
					pygame.mixer.music.set_volume(volume - 0.1)
					#print(volume)

		P1.handle_event(evento)
		screen.fill(White)
		screen.blit(P1.image, P1.rect)
		#screen.blit(viruses, (390, 110))




		pygame.display.update()
		clock.tick(20)
		#reloj.set_fps_limit(fps)
main()
pygame.quit()