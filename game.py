from player import *
from enemy import *
from bullet import *
from collision import *
bullet1 = bullet()
player1 = player()
enemy1 = enemy()

pygame.init()
print(player1.speed)
x = y = 0
clock = pygame.time.Clock()


while True:
	clock.tick(30)
	curr_event = pygame.event.poll()
	bullet1.draw(player1.pos,curr_event)
	player1.kbdraw(curr_event)
	enemy1.draw(player1.pos)
	pygame.display.update()
	if collidevec(enemy1.pos,bullet1.pos,50):
		enemy1.reset()
		enemy1 = enemy()
		bullet1.reset()
	if bullet1.pos.x > 1024 or bullet1.pos.x < 0 or bullet1.pos.y > 768 or bullet1.pos.y < 0:
		bullet1.reset()


