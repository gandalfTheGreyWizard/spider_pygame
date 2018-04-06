import random
from player import *

class enemy(object):
	pos_y = 0
	pos_x = 0
	pos = vector(0,0)
	speed = 5
	enemy_img = "enemy1.png"
	enemy_left = pygame.image.load(enemy_img).convert_alpha()
	enemy_right = pygame.transform.rotate(enemy_left,180)
	enemy_down = pygame.transform.rotate(enemy_left,90)
	enemy_up = pygame.transform.rotate(enemy_left,-90)
	enemy = enemy_up
	sprite_pos = (0,0)
	def __init__(self):
		i = random.choice([1,2])
		if i == 1:
			self.pos_y = random.choice([50,100,150,200,250,300,350,400,450,500,550,600])
			self.pos_x = random.choice([0,1024])
		else :
			self.pos_y = random.choice([0,768])
			self.pos_x = random.choice([50,100,200,300,400,500,600,700,800,900,1000])
		if self.pos_x == 1024:
			self.enemy = self.enemy_left
		if self.pos_x == 0:
			self.enemy = self.enemy_right
		if self.pos_y == 0:
			self.enemy = self.enemy_down
		if self.pos_y == 768:
			self.enemy = self.enemy_up
		self.pos = vector(self.pos_x,self.pos_y)
	def draw(self,vec_dest):
		direction = vec_dest - self.pos
		direction.normalize()
		self.pos += direction * self.speed
		self.sprite_pos = self.pos.tupleit()
		self.sprite_pos = (self.sprite_pos[0] - self.enemy.get_width()/2,self.sprite_pos[1] - self.enemy.get_height()/2)
		screen.blit(background,(self.sprite_pos[0] - 10,self.sprite_pos[1] - 10),pygame.Rect(self.sprite_pos[0]-10,self.sprite_pos[1]-10,100,100))
		screen.blit(self.enemy,self.sprite_pos)
	def reset(self):
		screen.blit(background,(self.sprite_pos[0] - 10,self.sprite_pos[1] - 10),pygame.Rect(self.sprite_pos[0]-10,self.sprite_pos[1]-10,100,100))
