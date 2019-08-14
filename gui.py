import pygame
import numpy as np
import random
import sys
import math
rows,columns = 6,7

khaki = ( 240,230,140)
darkOliveGreen = ( 85,107,47)
red = (255,0,0)
blue= (0,0,205)

player=925
pc=905

rectangleHeight=130
rectangleWidth=170
radius = 50
width=1180
height=910
size = (width, height)


player_1 = 1
player_2= 2
flag=False

screen = pygame.display.set_mode(size)
def initialization():
	board = np.zeros((rows,columns))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece



def makegui(board):
	for c in range(columns):
		for r in range(rows):
			pygame.draw.rect(screen, khaki, (c*rectangleWidth, r*rectangleHeight+rectangleHeight, rectangleWidth, rectangleHeight))
			pygame.draw.circle(screen, darkOliveGreen, (int(c*rectangleWidth+rectangleWidth/2), int(r*rectangleHeight+rectangleHeight+rectangleHeight/2)), radius)
	
	for c in range(columns):
		for r in range(rows):		
			if board[r][c] == player_1:
				pygame.draw.circle(screen, red, (int(c*rectangleWidth+rectangleWidth/2), height-int(r*rectangleHeight+rectangleHeight/2)), radius)
			elif board[r][c] == player_2: 
				pygame.draw.circle(screen, blue, (int(c*rectangleWidth+rectangleWidth/2), height-int(r*rectangleHeight+rectangleHeight/2)), radius)
	pygame.display.update()

board = initialization()
pygame.init()

makegui(board)
pygame.display.update()
turn = 925

myfont = pygame.font.SysFont("monospace", 75)
while not flag:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, darkOliveGreen, (0,0, width, rectangleHeight))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == player:
				posx = event.pos[0]
				col = int(math.floor(posx/rectangleWidth))
				posy= event.pos[1]
				#print(posy)
				row= int(math.floor(posy/rectangleHeight))

			drop_piece(board, row, col, player_1)
				

		

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, darkOliveGreen, (0,0, width, rectangleHeight))
			posx = event.pos[0]
			#print(posx)
			if turn == player:
				pygame.draw.circle(screen, red, (posx, int(rectangleHeight/2)), radius)
		if event.type == pygame.QUIT:
			sys.exit()

		pygame.display.update()


		