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
negInf=-math.inf
posInf=math.inf
connect=4
player_1 = 1
player_2= 2
flag=False
no_piece=0
screen = pygame.display.set_mode(size)


def validLocations(board):
	validLocation = []
	for col in range(columns):
		if isValid(board, col):
			validLocation.append(col)
	return validLocation

def getFreeRow(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r

def putPiece(board, row, col, piece):
	board[row][col] = piece

def checkAvailableRow(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r
def isValid(board, col):
	return board[rows-1][col] == 0

def myHeuristic(numberOfPiece):
	fact=math.factorial(numberOfPiece)
	return 3**fact


def countPieces(box, piece):
	score = 0
	opp_piece = player_1
	if piece == player_1:
		opp_piece = player_2
	if box.count(piece) == 2 and box.count(no_piece) == 2:
		score +=myHeuristic(2)

	elif box.count(piece) == 3 and box.count(no_piece) == 1:
		#print("window count")
		score +=myHeuristic(3)

	elif box.count(piece) == 4:
		score +=myHeuristic(7)

	if box.count(opp_piece) == 3:
		score -=myHeuristic(3)


	if box.count(piece)==1 and box.count(no_piece)==3:
		score+= myHeuristic(1)
		#print("placeing ", score)

	return score

def getScore(board, piece):
	score = 0

	#kunakuni
	for r in range(rows-3):
		for c in range(columns-3):
			box = [board[r+i][c+i] for i in range(connect)]
			score += countPieces(box, piece)

	#kunakuni
	for r in range(rows-3):
		for c in range(columns-3):
			box = [board[r+3-i][c+i] for i in range(connect)]
			score += countPieces(box, piece)

	#horizontal
	for r in range(rows):
		rowArray =list(board[r])
		#print(rowArray)
		for c in range(columns-3):
			box = rowArray[c:c+connect]
			score += countPieces(box, piece)

	## vertical
	for c in range(columns):
		#colArray = [int(i) for i in list(board[:,c])]
		col=list(zip(*board))
		colArray=list(col[c])
		for r in range(rows-3):
			box = colArray[r:r+connect]
			score += countPieces(box, piece)


	return score


def winning(board, piece):
	for c in range (4):
		for r in range(3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				print("kunakuni won")
				return True

	for c in range(4):
		for r in range(3, 6):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				print("kunakuni won")
				return True

	
	for c in range(4):
		for r in range(6):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				print("horizontally won")
				return True


	for c in range(7):
		for r in range(3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				print("vertically won")
				return True



def checkEnd(board):
	return winning(board, player_1) or winning(board, player_2) 

def minimax(board, depth, alpha, beta, maxNode):
	valid_locations=validLocations(board)
	#valid_locations=[0,1,2,3,4,5,6]
	#print(valid_locations)
	if checkEnd(board):
		if winning(board, player_2):
			return (None, 1000000)
		elif winning(board, player_1):
			return (None, -1000000)
		else: 
			return (None, 0)

	if depth==0:
		#print("akib ", getScore(board, player_2))
		return (None, getScore(board, player_2))
	if maxNode:
		
		tempBeta = negInf
		choose = random.choice(valid_locations)
		print(choose)

		for col in valid_locations:
			tempBoard = board.copy()
			row = checkAvailableRow(board, col)
			putPiece(tempBoard, row, col, player_2)
			noneed, newValue = minimax(tempBoard, depth-1, alpha, beta, False)
			#print(newValue)

			if newValue > tempBeta:
				tempBeta = newValue
				choose = col

			if alpha<tempBeta:
				alpha=tempBeta
			else:
				alpha=alpha
				#print(alpha)
			
			if alpha >= beta:
				#print("pruning done- 1")
				break
		return choose, tempBeta

	else: 
		tempAlpha = posInf
		choose = random.choice(valid_locations)

		for col in valid_locations:
			row = checkAvailableRow(board, col)
			tempBoard = board.copy()
			putPiece(tempBoard, row, col, player_1)
			noneed, amarValue = minimax(tempBoard, depth-1, alpha, beta, True)
			
			if amarValue < tempAlpha:
				tempAlpha = amarValue
				column = col
			
			if beta > tempAlpha:
				beta=tempAlpha
			else:
				beta=beta
			#beta = min(beta, tempAlpha)
			if alpha >= beta:
				#print("pruning done- 2")
				break
		return choose, tempAlpha

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

board = np.zeros((rows,columns))
pygame.init()

makegui(board)
pygame.display.update()
turn = 925
winner=""
font =pygame.font.SysFont("comicsansms", 150)

while not flag:
	if flag:

		pygame.time.wait(8000)
	
	if turn == pc:				

		col, minimaxValue= minimax(board, 5, -math.inf, math.inf, True)

		if isValid(board, col):
			#pygame.time.wait(500)
			row = getFreeRow(board, col)
			putPiece(board, row, col, player_2)

			if winning(board, player_2):
				winner="Computer wins!!"
				label = font.render(winner, 1, blue)
				screen.blit(label, (155,10))
				flag = True

			#print_board(board)
			makegui(board)

			turn =925
			print("turn pc", turn)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, darkOliveGreen, (0,0, width, rectangleHeight))
			if turn == player:
				posx = event.pos[0]
				col = int(math.floor(posx/rectangleWidth))
				if isValid(board, col):
					row = checkAvailableRow(board, col)
					putPiece(board, row, col, player_1)

					if winning(board, player_1):
						winner="HUMAN wins!!"
						label = font.render(winner, 1, red)
						screen.blit(label, (155,10))
						flag = True

					turn =905

					makegui(board)


		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, darkOliveGreen, (0,0, width, rectangleHeight))
			posx = event.pos[0]
			#print(posx)
			if turn == player:
				pygame.draw.circle(screen, red, (posx, int(rectangleHeight/2)), radius)

		pygame.display.update()


		