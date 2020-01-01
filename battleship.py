from time import sleep
import os

n    = int(input("Plss Enter the size of map(example: '3' for 3x3 map, min = 3)\n"))
cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']


s_hit  = 0
r_ship = 0

player1_board, player2_board = [[" " for x in range(n)] for y in range(n)], [[" " for x in range(n)] for y in range(n)]

def boardPrinter(board, m):
	s = (m*4)+1
	print('\n\t%s'%(' '*(2)), end='')
	for i in range(m):
		print('%d%s'%(i+1, ' '*3), end='')
	print('')		
	for i in range(m):
		print('\t', end='')
		print("_"*s)
		print('%s\t|'%cols[i], end='')
		for j in range(m):
			print(' %s '%board[i][j], end="|")
		print('')
	print('\t', end='')		
	print("_"*s)

def playerMove(player_board, n):
	global r_ship
	boardPrinter(player_board, n)
	for i in range(5):
		print("Remaining ships: %d"%(5-i))
		ship_place = input("Where do u want to place ur ship?? (example: 'A2')(Hit Enter to pass it!)\n")
		try:
			player_board[cols.index(ship_place[:1].upper())][int(ship_place[1:])-1] = 'S'
			r_ship += 1
		except:
			print("Enter Valid location!")
		os.system("clear")
		boardPrinter(player_board, n)
	sleep(2)	


def playerAttack(player2_board_attacker, player1_board_target, n):
	global s_hit, r_ship
	boardPrinter(player2_board_attacker, n)
	for i in range(5):
		print("Remaining bombs: %d"%(5-i))
		bomb_place = input("Where do u wnat to drop a bomb?? (example: 'A2')(Hit Enter to pass it!)\n")
		if bomb_place is '': 
			os.system('clear')
			boardPrinter(player2_board_attacker, n)
			continue
		if player1_board_target[cols.index(bomb_place[:1].upper())][int(bomb_place[1:])-1] is 'S':
			os.system('clear')
			print("\nWell done!\nu hit the ship!")
			s_hit += 1
			r_ship -= 1
			player2_board_attacker[cols.index(bomb_place[:1].upper())][int(bomb_place[1:])-1] = 'X'
		else:
			os.system('clear')
			print("\nWhoooooppppsss!!, wrong place!\ntry another location")

		boardPrinter(player2_board_attacker, n)

while True:
	xd = input("READY PLAYER1???(y/n)")
	if xd is 'y' or xd is 'Y':
		break
	else:
		print("GET READY :|")

os.system('clear')
playerMove(player1_board, n)
os.system('clear')

while True:
	xd = input("READY PLAYER2???(y/n)")
	if xd is 'y' or xd is 'Y':
		break
	else:
		print("GET READY :|")

os.system('clear')
playerAttack(player2_board, player1_board, n)
os.system('clear')

print('\nPlayer1 board:')
boardPrinter(player1_board, n)	
print('\nPlayer2 board:')
boardPrinter(player2_board, n)

if r_ship == 0 and s_hit > 0:
	print("--> player2 WON!")
else:
	print("--> player1 WON!")

print('GG-WP!')	