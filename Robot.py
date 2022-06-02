'''
The class implementing a robot moving in an infinite 2-dimensional space.
'''
class Robot:
	def __init__(self):
		self.row_pos = 0
		self.col_pos = 0
		heading = 0

	def __init__(self, row_pos, col_pos, heading):
		self.row_pos = row_pos
		self.col_pos = col_pos
		self.heading = heading

	def turn(turn_instruction):
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

	def move(move_instruction):
		if move_instruction == 'front':
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
		elif move_instruction == 'back':
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

	def print_pos():
		heading_directions = {0:'south', 1:'west', 2:'north', 3:'east'}
		print('My current row position is {row_pos}'.format(row_pos = self.row_pos))
		print('My current column position is {col_pos}'.format(col_pos = self.col_pos))
		print('My current heading is {heading}'.format(heading = heading_directions[self.heading]))