from collections import deque

class Robot:
	''' A class implementing a robot moving in an infinite 2D space. '''
	def __init__(self, row_position = 0, column_position = 0, heading = 0):
		'''
		Parametrized constructor.
		
		Parameters:
		row_position (int): the row position of the robot
		col_position (int): the column position of the robot
		heading (int): the heading of the robot. It can only take four values [0, 1, 2, 3] that correspond to the directions [south, west, north, east]
		
		'''
		self.row_position = row_position
		self.column_position = column_position
		self.heading = heading
		self.heading_directions = {0:'south', 1:'west', 2:'north', 3:'east'}	# for transforming integer heading to string
		self.positions_history = deque()	# queue that holds the past positions of the robot

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
		self.positions_history.append((self.row_position, self.column_position, self.heading))

	def move(self, move_instruction):
		'''
		Robot move forward or backward.

		Parameters:
		move_instruction (str): the move instruction coming from the end user. It can either be 'forward' or 'backward'
		
		'''
		if move_instruction == 'forward':
			if self.heading == 0:
				self.row_position += 1
			elif self.heading == 1:
				self.column_position -= 1
			elif self.heading == 2:
				self.row_position -= 1
			elif self.heading == 3:
				self.column_position += 1
			else:
				pass
		elif move_instruction == 'backward':
			if self.heading == 0:
				self.row_position -= 1
			elif self.heading == 1:
				self.column_position += 1
			elif self.heading == 2:
				self.row_position += 1
			elif self.heading == 3:
				self.column_position -= 1
			else:
				pass
		else:
			pass
		self.positions_history.append((self.row_position, self.column_position, self.heading))

	def print_history(self):
		''' Prints the history of past positions of the robot (from oldest to current). '''

		# we need a temp queue to store the positions dequeued from the history queue
		temp_positions_history = deque()
		positions_history_length = len(self.positions_history)
		while positions_history_length != 0:
			past_position = self.positions_history.popleft()
			past_row_position = past_position[0]
			past_column_position = past_position[1]
			past_heading = past_position[2]

			print('({row_position}, {column_position}, {heading})'.format(row_position = past_row_position, column_position = past_column_position, heading = self.heading_directions[past_heading]), end='')
			if positions_history_length != 1:
				print(' -> ', end='')
			temp_positions_history.append(past_position)
			positions_history_length = len(self.positions_history)

		# enqueue past positions back to the history queue
		temp_positions_history_length = len(temp_positions_history)
		while temp_positions_history_length != 0:
			self.positions_history.append(temp_positions_history.popleft())
			temp_positions_history_length = len(temp_positions_history)

		# for pretty-printing
		print('\n')

	def print_pos(self):
		''' Prints the current position of the robot. '''
		print('------ Current Position ------')
		print('({row_position}, {column_position}, {heading})'.format(row_position = self.row_position, column_position = self.column_position, heading = self.heading_directions[self.heading]))
		print()