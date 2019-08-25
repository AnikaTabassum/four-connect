import numpy as np
import random
#import pygame
import sys
import math

def putPiece(board, row, col, piece):
	board[row][col] = piece

def checkForFreeRow(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r
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
		print("placeing ", score)

	return score

def getScore(board, piece):
	score = 0
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
		print(rowArray)
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
	#kunakuni

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

	valid_locations=[0,1,2,3,4,5,6]
	print(valid_locations)
	if depth==0:
		print("depth 0.. .returning..........")
		return (None, getScore(board,player_2))
	if maxNode:

		tempBeta = negInf
		choose = random.choice(valid_locations)
		print(choose)

		for col in valid_locations:
			tempBoard = board.copy()
			row = checkForFreeRow(board, col)
			putPiece(tempBoard, row, col, player_2)
			newValue = minimax(tempBoard, depth-1, alpha, beta, False)[1]
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
				print("pruning done- 1")
				break
		return choose, tempBeta

	else:
		tempAlpha = posInf
		choose = random.choice(valid_locations)

		for col in valid_locations:
			row = checkForFreeRow(board, col)
			tempBoard = board.copy()
			putPiece(tempBoard, row, col, player_1)
			amarValue = minimax(tempBoard, depth-1, alpha, beta, True)[1]

			if amarValue < tempAlpha:
				tempAlpha = amarValue
				column = col

			if beta > tempAlpha:
				beta=tempAlpha
			else:
				beta=beta
			#beta = min(beta, tempAlpha)
			if alpha >= beta:
				print("pruning done- 2")
				break
		return choose, tempAlpha
negInf=-math.inf
posInf=math.inf

rows = 6
columns = 7
no_piece=0
player_1 = 1     ## computer
player_2= 2 ######## manush
board = np.zeros((rows,columns))
connect=4
minimax(board, 5, negInf,posInf, True)