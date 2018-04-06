import pygame
def evnt(type,key)
	for event in pygame.event.get():
		event_type = str(event.type)
		event_key = str(event.key)