import numpy as np
import math
import random
negInf=-math.inf
posInf=math.inf

rows, columns=6,7

PLAYER = 925
AI = 905

EMPTY = 0
player_1 = 1
player_2= 2

WINDOW_LENGTH = 4
def initialization():
	board = np.zeros((rows,columns))
	minimax(board, 5, negInf, posInf, True)
	return board

def checkForFreeRow(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r

def isValid(board, col):
	return board[rows-1][col] == 0



def checkEnd(board):
	return winning(board, player_1) or winning(board, player_2) or len(getValid(board)) == 0

def putPiece(board, row, col, piece):
	board[row][col] = piece




def minimax(board, depth, alpha, beta, maxNode):
	validPositions = getValid(board)
	print(validPositions)
	if maxNode:
		choose = random.choice(validPositions)
		tempBeta = negInf

		for col in validPositions:
			tempBoard = board.copy()
			row = checkForFreeRow(board, col)

			putPiece(tempBoard, row, col, player_2)

			newValue = minimax(tempBoard, depth-1, alpha, beta, False)[1]

			if newValue > tempBeta:
				tempBeta = newValue
				choose = col

			if alpha>tempBeta:
				tempBeta=alpha
			else:
				alpha=alpha
				print(alpha)
			if alpha >= beta:
				print("pruning done- 1")
				break
		return choose, tempBeta

	else: 
		tempAlpha = posInf
		choose = random.choice(validPositions)

		for col in validPositions:
			row = checkForFreeRow(board, col)

			tempBoard = board.copy()
			
			putPiece(tempBoard, row, col, player_1)
			
			newValue = minimax(tempBoard, depth-1, alpha, beta, True)[1]
			
			if newValue < tempAlpha:
				tempAlpha = newValue
				column = col
			
			if beta < tempAlpha:
				tempAlpha=beta
			else:
				beta=beta

			if alpha >= beta:
				print("pruning done- 2")
				break
		return choose, tempAlpha


	if checkEnd(board):

		if winning(board, player_1):
			return (None, -905)

		elif winning(board, player_2):
			return (None, 905)
		else:
			return (None, 0)
			
	if depth==0:
		print("sesehhhh")
		return 0
	

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

		

def getValid(board):
	validPositions = []
	for col in range(columns):
		if isValid(board, col):
			validPositions.append(col)
	return validPositions

board = initialization()

