class Robot:
	''' A class implementing a robot moving in an infinite 2D space. '''
	def __init__(self, row_pos = 0, col_pos = 0, heading = 0):
		'''
		Parametrized constructor.
		
		Parameters:
		row_pos (int): the row position of the robot
		col_pos (int): the column position of the robot
		heading (int): the heading of the robot. It can only take four values [0, 1, 2, 3] that correspond to the directions [south, west, north, east]
		
		'''
		self.row_pos = row_pos
		self.col_pos = col_pos
		self.heading = heading

	def turn(self, turn_instruction):
		'''
		Robot turn right or left.

		Parameters:
		turn_instruction (str): the turn instruction coming from the end user. It can either be 'right' or 'left'
		
		'''
		if turn_instruction == 'right':
			self.heading += 1
			if self.heading == 4:
				self.heading = 0
		elif turn_instruction == 'left':
			self.heading -= 1
			if self.heading == -1:
				self.heading = 3
		else:
			pass

	def move(self, move_instruction):
		'''
		Robot move forward or backward.

		Parameters:
		move_instruction (str): the move instruction coming from the end user. It can either be 'forward' or 'backward'
		
		'''
		if move_instruction == 'forward':
			if self.heading == 0:
				self.row_pos += 1
			elif self.heading == 1:
				self.col_pos -= 1
			elif self.heading == 2:
				self.row_pos -= 1
			elif self.heading == 3:
				self.col_pos += 1
			else:
				pass
		elif move_instruction == 'backward':
			if self.heading == 0:
				self.row_pos -= 1
			elif self.heading == 1:
				self.col_pos += 1
			elif self.heading == 2:
				self.row_pos += 1
			elif self.heading == 3:
				self.col_pos -= 1
			else:
				pass
		else:
			pass

	def print(self):
		'''
		Prints the current position of the robot.

		'''
		heading_directions = {0:'south', 1:'west', 2:'north', 3:'east'}
		print('------ Current Position ------')
		print('({row_pos}, {col_pos}, {heading})'.format(row_pos = self.row_pos, col_pos = self.col_pos, heading = heading_directions[self.heading]))
		print()