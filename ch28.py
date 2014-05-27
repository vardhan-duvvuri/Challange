def tictactoe(moves):
	
	if moves[0][0] == moves[0][1] == moves[0][2]:
		return "\'%s\' wins (horizontal)."%(moves[0][0])
	elif moves[1][0] == moves[1][1] == moves[1][2]:
                return "\'%s\' wins (horizontal)."%(moves[1][0])
	elif moves[2][0] == moves[2][1] == moves[2][2]:
                return "\'%s\' wins (horizontal)."%(moves[2][0])
	elif moves[0][0] == moves[1][0] == moves[2][0]:
                return "\'%s\' wins (vertical)."%(moves[0][0])
	elif moves[0][1] == moves[1][1] == moves[2][1]:
                return "\'%s\' wins (vertical)."%(moves[0][1])
	elif moves[0][2] == moves[1][2] == moves[2][2]:
                return "\'%s\' wins (vertical)."%(moves[0][2])
	elif moves[0][0] == moves[1][1] == moves[2][2]:
                return "\'%s\' wins (diagonal)."%(moves[0][0])
	elif moves[0][2] == moves[1][1] == moves[2][0]:
                return "\'%s\' wins (diagonal)."%(moves[0][2])
	else:
		return "Draw."



if __name__ == "__main__":
	print tictactoe([('X', ' ', 'O'), 
                   (' ', 'O', 'O'), 
                   ('X', 'X', 'X') ])
	print tictactoe([('X', 'O', 'X'), 
                   ('O', 'X', 'O'), 
                   ('O', 'X', 'O') ])
	print tictactoe([('X', 'O', 'O'), 
                   ('X', 'O', ' '), 
                   ('O', 'X', ' ') ])
	print tictactoe([('X', 'O', 'X'), 
                   ('O', 'O', 'X'), 
                   ('O', 'X', 'X') ])
