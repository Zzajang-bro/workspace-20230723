import traceback


try:
	import ctypes
	myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	import os
	os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

	import urllib.request

	# aisaka/ blueMoon/ earth/ honeycomb/ hoshino/ hoshino2/ naisho
	# if not os.path.exists('./wallpaper.jpg'):
	bgNm = 'blueMoon'
	if True:
		imgURL = f'http://small.23jhj.com/Zzajang-bro/workspace/wallpapers/{bgNm}.jpg'
		urllib.request.urlretrieve(imgURL, "./wallpaper.jpg")

	import pygame
	import pygame.gfxdraw
	import pygame.freetype

	pygame.init()
	screen = pygame.display.set_mode((0,0))
	clock = pygame.time.Clock()

	pygame.display.set_caption('Zzajang-bro workspace')
	pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

	D2 = pygame.freetype.SysFont('Neo둥근모', 12)

	bg = pygame.transform.scale( pygame.image.load('./wallpaper.jpg'), screen.get_size() )
	pygame.gfxdraw.box(bg, ((0,0),bg.get_size()), (0,0,0,120))

	icon = pygame.image.load('./res/Zzajang_bro.logo.png')
	pygame.display.set_icon(icon)

	folderIcon = pygame.transform.scale( pygame.image.load('./res/folder.png'), (48,48) )

	def draw():
		pass

	mouseX, mouseY = 0, 0

	closeButtonX = 1060
	closeButtonY = 10

	while True:

		quitMsgFlag = False
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				quitMsgFlag = True
			else:
				if e.type == pygame.MOUSEMOTION:
					mouseX, mouseY = e.pos

		if quitMsgFlag:
			break

		screen.blit(bg, (0,0) )
		screen.blit(folderIcon, (50,50))
		pygame.gfxdraw.rectangle(screen, (mouseX, mouseY, 10, 10), (123,123,123))
		#D2.render_to(screen, (50,100), '새 창 열기', fgcolor=(255,255,255), size=12)

		x = []
		for i in range(len(pygame.key.get_pressed())):
			if pygame.key.get_pressed()[i]:
				x.append(i)
		#x = [ 'T' if b else 'F' for b in pygame.key.get_pressed()]
		D2.render_to(screen, (50, 120), str(x), fgcolor=(255,255,255), size=12)
		# D2.render_to(screen, (50, 130), pygame.K_a, fgcolor=(255,255,255), size=12)

		clock.tick(60)
		pygame.display.flip()
	pygame.quit()

except:
	print(traceback.format_exc())
	input()