import pygame
import numpy as np
import random
import sys

rows,columns = 6,7

khaki = ( 240,230,140)
darkOliveGreen = ( 85,107,47)


player=925
ai=905

rectangleHeight=130
rectangleWidth=170
radius = 50
width=1180
height=910
size = (width, height)

EMPTY = 0
player_1 = 1
player_2= 2
flag=False

screen = pygame.display.set_mode(size)
def initialization():
	board = np.zeros((rows,columns))
	return board

def makegui(board):
	for c in range(columns):
		for r in range(rows):
			pygame.draw.rect(screen, khaki, (c*rectangleWidth, r*rectangleHeight+rectangleHeight, rectangleWidth, rectangleHeight))
			pygame.draw.circle(screen, darkOliveGreen, (int(c*rectangleWidth+rectangleWidth/2), int(r*rectangleHeight+rectangleHeight+rectangleHeight/2)), radius)
	
	pygame.display.update()

board = initialization()
pygame.init()

makegui(board)
pygame.display.update()

while not flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
