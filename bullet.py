from player import *
class bullet(object):
	bullet_move = vector(0,0)
	pos = vector(0,0)
	bullet_img = "web.png"
	bullet = pygame.image.load(bullet_img).convert_alpha()
	count = 0
	sprite_pos = (0,0)
	flag = 0
	def draw(self,pos,event):
		if self.count == 0:
			self.pos = pos
		if event.type == KEYDOWN:
			if self.flag == 0:
				if event.key == K_a:
					self.bullet_move = vector(-10.0)
				if event.key == K_d:
					self.bullet_move = vector(10,0)
				if event.key == K_w:
					self.bullet_move = vector(0,-10)
				if event.key == K_s:
					self.bullet_move = vector(0,10)
				if event.key == K_SPACE:
					self.flag = 1
					self.count = 1
		if self.flag == 1:
			self.pos += self.bullet_move
			self.sprite_pos = self.pos.tupleit()
			self.sprite_pos = (self.sprite_pos[0] - self.bullet.get_width()/2,self.sprite_pos[1] - self.bullet.get_height()/2)
			screen.blit(background,(self.sprite_pos[0] - 10,self.sprite_pos[1] - 10),pygame.Rect(self.sprite_pos[0]-10,self.sprite_pos[1]-10,50,50))
			screen.blit(self.bullet,self.sprite_pos)
	def reset(self):
		screen.blit(background,(self.sprite_pos[0] - 10,self.sprite_pos[1] - 10),pygame.Rect(self.sprite_pos[0]-10,self.sprite_pos[1]-10,50,50))
		self.bullet_move = vector(0,0)
		self.pos = vector(0,0)
		self.count = 0
		self.flag = 0