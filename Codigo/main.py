import sys
import pygame
import pyglet.clock

pygame.init()

size = 800, 600 
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bolim')

fps = 60
Black = (0, 0, 0)
White = (255, 255, 255)


def main():
	reloj = pyglet.clock.Clock()
	reloj.set_fps_limit(fps)
	quit = False


	while quit != True:

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit = True





		pygame.display.update()
main()
pygame.quit()