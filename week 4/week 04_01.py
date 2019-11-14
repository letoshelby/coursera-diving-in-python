# magic methods.py
import os
import tempfile


class File:

	def __init__(self, tmp):
		self.tmp = tmp

	def write(self, text):
		with open(self.tmp, 'w') as f:
			f.write(text)

	def __str__(self):
		return self.tmp

	def __add__(self, obj):
		file_tmp = os.path.join(tempfile.gettempdir(), 'new_obj.txt')
		with open(file_tmp, 'w') as outfile:
			for file_name in [self.tmp, obj.tmp]:
				with open(file_name, 'r') as infile:
					outfile.write(infile.read())

		new_object = File(file_tmp)
		return new_object

	def __iter__(self):
		self.current = 0
		with open(self.tmp, 'r') as f:
			self.lines = f.readlines()
		return self

	def __next__(self):
		if self.current >= len(self.lines):
			raise StopIteration

		result = self.lines[self.current]
		self.current += 1
		return result