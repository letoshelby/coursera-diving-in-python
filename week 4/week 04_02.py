# Задание по программированию: Дескриптор с комиссией

class Value:

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, object, value):
		self.value = value - value * object.commission


class Account:
	amount = Value()

	def __init__(self, commission):
		self.commission = commission




