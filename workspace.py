import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import pygame.gfxdraw
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((0,0))
clock = pygame.time.Clock()

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

D2 = pygame.freetype.SysFont('D2Coding', 12)

def draw():
	pass

mouseX, mouseY = 0, 0

while True:

	quitMsgFlag = False
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			quitMsgFlag = True
		else:
			if e.type == pygame.MOUSEMOTION:
				mouseX, mouseY = e.pos
			pass
	if quitMsgFlag:
		break

	screen.fill((30,30,30))
	pygame.gfxdraw.rectangle(screen, (mouseX, mouseY, 10, 10), (123,123,123))
	D2.render_to(screen, (50,50), 'wow', fgcolor=(255,255,255), size=12)

	clock.tick(60)
	pygame.display.flip()
pygame.quit()
