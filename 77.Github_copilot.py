
def print_board(board):
	print("\n")
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_win(board, player):
	# Check rows, columns and diagonals
	for i in range(3):
		if all([cell == player for cell in board[i]]):
			return True
		if all([board[j][i] == player for j in range(3)]):
			return True
	if all([board[i][i] == player for i in range(3)]):
		return True
	if all([board[i][2 - i] == player for i in range(3)]):
		return True
	return False

def check_draw(board):
	return all([cell != ' ' for row in board for cell in row])

def main():
	board = [[' ' for _ in range(3)] for _ in range(3)]
	current_player = 'X'
	while True:
		print_board(board)
		try:
			move = input(f"Player {current_player}, enter your move (row and column 1-3, e.g. 1 3): ")
			row, col = map(int, move.split())
			row -= 1
			col -= 1
			if board[row][col] != ' ':
				print("Cell already taken. Try again.")
				continue
			board[row][col] = current_player
		except (ValueError, IndexError):
			print("Invalid input. Please enter row and column as two numbers between 1 and 3.")
			continue
		if check_win(board, current_player):
			print_board(board)
			print(f"Player {current_player} wins!")
			break
		if check_draw(board):
			print_board(board)
			print("It's a draw!")
			break
		current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
	main()
