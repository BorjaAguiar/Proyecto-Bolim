import sys
import pygame
import pyglet.clock

pygame.init()

size = 1280, 720 
icon = pygame.image.load('..\Arte\Grafico\Icon\icono.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bolim')
pygame.display.set_icon(icon)

fps = 60
Black = (0, 0, 0)
White = (255, 255, 255)


def main():
	reloj = pyglet.clock.Clock()
	reloj.set_fps_limit(fps)
	quit = False
	full_screen = False
	viruses = pygame.image.load('..\Arte\Grafico\Icon\icono.png')
	power = open('..\Data\power.txt', 'r')
	pygame.mixer.music.load('..\Arte\Audio\Feelings-8-bit.wav')
	pygame.mixer.music.play(100000)
	pygame.mixer.music.set_volume(0.5)
	

	while quit != True:

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

		screen.fill(White)
		screen.blit(viruses, (390, 110))




		pygame.display.update()
main()
pygame.quit()