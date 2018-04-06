def colbound(pos,sprite):
	colbound = (pos.x,pos.y,pos.x+sprite.get_width(),pos.y+sprite.get_height())
	return colbound
def ifcollision(sprite1,sprite2):
	if sprite2[0] < sprite1[2] and sprite2[0] > sprite1[0] and sprite2[3] > sprite1[1] and sprite2[3] < sprite1[3] and sprite2[1] < sprite1[3] and sprite2[1] > sprite1[1]:
		return True
	elif sprite2[2] > sprite1[0] and sprite2[2] < sprite1[2] and sprite2[3] > sprite1[1] and sprite2[3] < sprite1[3] and sprite2[1] < sprite1[3] and sprite2[1] > sprite1[1]:
		return True
	else:
		return False 
def collidevec(vec1,vec2,dist):
	vec3 = vec2 - vec1
	vec3_mag = vec3.magnitude()
	if vec3_mag < dist :
		return True
	else:
		return False