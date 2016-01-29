#!/usr/bin/python 
import math, pygame, tutorial

pygame.init()
window = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("Air-Raid Warning")
screen = pygame.Surface((1024, 600))

background = pygame.image.load('/usr/share/games/AirRaidWarning/resources/decor/background.png')
logo = pygame.image.load('/usr/share/games/AirRaidWarning/resources/decor/MainMenu/logo.png')
MainMenuLow = ['/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu1low.png',
				'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu2low.png',
				'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu3low.png',
				'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu4low.png',
				'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu5low.png']
MainMenuHight = ['/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu1hight.png',
					'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu2hight.png',
					'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu3hight.png',
					'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu4hight.png',
					'/usr/share/games/AirRaidWarning/resources/decor/MainMenu/menu5hight.png']
for i in range(0, 5):
	MainMenuLow[i] = pygame.image.load(MainMenuLow[i])
for i in range(0, 5):
	MainMenuHight[i] = pygame.image.load(MainMenuHight[i])
pygame.mixer.music.load('/usr/share/games/AirRaidWarning/resources/sounds/arw.ogg')
pygame.mixer.music.play()
	
done = True
while done:
	for i in pygame.event.get():
		done = done and (i.type != pygame.QUIT)
	pos = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	window.blit(screen, (0, 0))
	screen.fill((60,50,255))
	pygame.display.flip()
	
	screen.blit(background, (0,0))
	screen.blit(logo, (550,30))
	x = 724
	y = 260
	for i in range(0, 5):
		screen.blit(MainMenuLow[i], (x,y + i*60))
	if 724 < pos[0] < 974:
		for i in range(0, 5):
			if y + i*60 < pos[1] < y + i*60 + 50:
				screen.blit(MainMenuHight[i], (x,y + i*60))
				if i == 0 and click[0] == 1:
						pygame.mixer.music.stop()
						tutorial.tutor(window, screen)
				if i == 4 and click[0] == 1:
						done = False

	
	pos = pygame.mouse.get_pos()
  	psx, psy = pos[0], pos[1]
	#pygame.time.delay(1200)

