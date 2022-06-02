from Robot import Robot


def main():
	''' The starting point of the Robot application. '''
	robot = Robot()
	while True:
		try:
			instruction = input('What to do? Type \'move\' for moving, \'turn\' for turning, \'print\' for printing the current position of the robot and \'hist\' for printing the history of positions of the robot.\n')
			print()
			
			# verifying the input instruction will either be 'move' or 'turn'
			while instruction != 'move' and instruction != 'turn' and instruction != 'print' and instruction != 'hist':
				instruction = input('Wrong instruction. Type \'move\' for moving, \'turn\' for turning, \'print\' for printing the current position of the robot and \'hist\' for printing the history of positions of the robot.\n')
			
			if instruction == 'move':
				move_instruction = input('Forward or backward? Type \'forward\' for forward and \'backward\' for backward\n')

				# verifying the move instruction is either 'forward' or 'backward'
				while move_instruction != 'forward' and move_instruction != 'backward':
					move_instruction = input('Wrong move instruction. Type \'forward\' for forward and \'backward\' for backward\n')

				robot.move(move_instruction)
				print()

			elif instruction == 'turn':
				turn_instruction = input('Right or left? Type \'right\' for right and \'left\' for left\n')

				# verifying the turn instruction is either 'right' or 'left'
				while turn_instruction != 'right' and turn_instruction != 'left':
					turn_instruction = input('Wrong turn instruction. Type \'right\' for right and \'left\' for left\n')

				robot.turn(turn_instruction)
				print()

			elif instruction == 'print':
				robot.print_pos() 

			elif instruction == 'hist':
				robot.print_history()

			else:
				pass
		except KeyboardInterrupt:
			break

	print('\nGoodbye!')


if __name__ == '__main__':
	main()