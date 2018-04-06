from vector import *
import pygame
from pygame.locals import *
from sys import exit
screen = pygame.display.set_mode((1024,768),HWSURFACE|DOUBLEBUF,32)


background_img = "background.png"
background = pygame.image.load(background_img).convert()
screen.blit(background,(0,0))
class player(object):
	pos = vector(0,0)
	move_vec = vector(0,0)
	speed = 5
	hist_key = K_1
	player_img = "player1.png"
	player_sprite_right = pygame.image.load(player_img).convert_alpha()
	player_sprite_up = pygame.transform.rotate(player_sprite_right,90)
	player_sprite_down = pygame.transform.rotate(player_sprite_right,-90)
	player_sprite_left = pygame.transform.rotate(player_sprite_right,180)
	player_sprite = player_sprite_right
		
	def click_draw(self,destination):
		direction = destination - self.pos
		direction.normalize()
		self.pos += direction*self.speed
		pos = self.pos.tupleit()
		screen.blit(self.player_sprite,pos)
	def kbdraw(self,event):
		
		if event.type == KEYDOWN:
			if event.key == K_w:
				self.hist_key = event.key
				self.move_vec = vector(0,-5)
				self.player_sprite = self.player_sprite_up
			if event.key == K_s:
				self.hist_key = event.key
				self.move_vec = vector(0,5)
				self.player_sprite = self.player_sprite_down
			if event.key == K_d:
				self.hist_key = event.key
				self.move_vec = vector(5,0)
				self.player_sprite = self.player_sprite_right
			if event.key == K_a:
				self.hist_key = event.key
				self.move_vec = vector(-5,0)
				self.player_sprite = self.player_sprite_left
			if event.key == K_ESCAPE:
				exit()
		if event.type == KEYUP and event.key == self.hist_key:
				self.move_vec = vector(0,0)

		self.pos += self.move_vec

		sprite_pos = self.pos.tupleit()
		sprite_pos = (sprite_pos[0] - self.player_sprite.get_width()/2,sprite_pos[1] - self.player_sprite.get_height()/2)
		screen.blit(background,(sprite_pos[0] - 5,sprite_pos[1] - 5),pygame.Rect(sprite_pos[0]-5,sprite_pos[1]-5,60,60))
		screen.blit(self.player_sprite,sprite_pos)




		