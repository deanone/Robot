'''
The starting point of the Robot application.
'''
from Robot import Robot


def main():
	while True:
		robot = Robot()
		instruction = input('What to do? Type \'move\' for moving and \'turn\' for turning\n')
		if instruction == 'move':
			move_instruction = input('Forward or backward? Type \'front\' for forward and \'back\' for backward\n')
			robot.move(move_instruction)
		elif instruction == 'turn':
			turn_instruction = input('Right or left? Type \'right\' for right and \'left\' for left\n')
			robot.turn(turn_instruction)
		else:
			print('Type \'move\' for moving and \'turn\' for turning')


if __name__ == '__main__':
	main()