#!/usr/bin/python 
import pygame, math, os

class Sprite:
	def __init__(self,xpos,ypos,xspeed,yspeed,angle,filename):
		self.x=xpos
		self.y=ypos
		self.xs = xspeed;
		self.ys = yspeed;
		self.angle = angle;
		self.bitmap=pygame.image.load(filename)
		self.bitmap.set_colorkey((255,255,255))
		self.rect = self.bitmap.get_rect()
	def render(self, screen):
		screen.blit(self.bitmap,(self.x, self.y))
		#a = pygame.transform.rotate(self.bitmap, self.angle-90).get_rect(center=self.rect.center)
		#screen.blit(pygame.transform.rotate(self.bitmap, self.angle-90), (a[0] + self.x, a[1] + self.y))
	def move(self):
		self.x += self.xs
		self.y += self.ys
	def speed(self, sp):
		self.xs = math.sin(self.angle/57.2958) * sp
		self.ys = math.cos(self.angle/57.2958) * sp


class Player:
	def __init__(self,xpos,ypos,angle,h,xspeed,yspeed,filename):
		self.x=xpos
		self.y=ypos
		self.angle = angle
		self.xs = xspeed
		self.ys = yspeed
		self.h = h
		self.bitmap=pygame.image.load(filename)
		self.bitmap.set_colorkey((255,255,255))
		self.rect = self.bitmap.get_rect()
	def setAngle(self, angle):
		if(abs(self.angle - angle) < 3):
			return
		a = angle - self.angle
		t = a
		if abs(a) > 180:
			t = 360 - abs(a)
			if a >= 0:
				t *= -1
		t = abs(t)/t * math.sqrt(abs(t))/11
		self.angle += t
		if self.angle > 180:
			self.angle -= 360
		if self.angle < (-180):
			self.angle += 360
	def render(self, screen):
		a = pygame.transform.rotate(self.bitmap, self.angle-90).get_rect(center=self.rect.center)
		screen.blit(pygame.transform.rotate(self.bitmap, self.angle-90), (a[0] + self.x, a[1] + self.y))
	def move(self):
		self.h -= self.ys
	def speed(self, sp):
		self.xs = math.sin(self.angle/57.2958) * sp
		self.ys = math.cos(self.angle/57.2958) * sp #* math.sqrt( max((self.h - 500)/(-500), 0.1) )



def tutor(window, screen):
	planer = Player(350, 210, 90, 0, 0, 90,'/usr/share/games/AirRaidWarning/resources/models/warplanes/B17/B17R.gif')
	t = 0;
	st = 0;
	psx = 0;
	psy = 0;
	ground = [1, 2, 3]
	for i in range(0, 3):
		ground[i] = Sprite(0, 401, 0, 0, 0, '/usr/share/games/AirRaidWarning/resources/maps/TestMap/ground.png')
	sky = pygame.image.load('/usr/share/games/AirRaidWarning/resources/maps/TestMap/sky.png')
	done = True
	while done and ground[0].y > 250:
		pygame.event.get()
		#for i in pygame.event.get():
		done = done and (pygame.key.get_pressed()[pygame.K_ESCAPE] == 0)
		window.blit(screen, (0, 0))
		screen.fill((60,50,255))
		screen.blit(sky, (0, 0))
		
		if abs(ground[0].x + 1000) > 1000:
			ground[0].x = -1000
		if abs(ground[1].x) > 1000:
			ground[1].x = 0
		if abs(ground[2].x - 1000) > 1000:
			ground[2].x = 1000
		for i in range(0, 3):
			ground[i].render(screen)

		pygame.display.flip()
		pos = pygame.mouse.get_pos()
  		psx = pos[0] - 500
  		psy = max(pos[1] - 250, planer.h - 1000)
		angle = math.atan2(psx, psy) * 57.2958
		planer.setAngle(angle)

		if planer.angle > 0:
			planer.bitmap=pygame.image.load('/usr/share/games/AirRaidWarning/resources/models/warplanes/B17/B17R.gif')
		else:
			planer.bitmap=pygame.image.load('/usr/share/games/AirRaidWarning/resources/models/warplanes/B17/B17L.gif')
		planer.bitmap.set_colorkey((255,255,255))


		planer.speed(11)
		planer.move()
		planer.render(screen)

		for i in range(0, 3):
			ground[i].x -= planer.xs
			ground[i].y -= planer.ys

		print planer.h, " ", psy

		pygame.time.delay(10)
