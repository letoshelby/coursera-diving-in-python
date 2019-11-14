import socket
import time


class Client:

	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout
		try:
			self.connection = socket.create_connection((self.host, self.port))
		except socket.error as err:
			raise ClientError('error create connection', err)

	def read_data(self):
		"""Читаем ответ сервера"""

		data = b''
		while not data.endswith(b'\n\n'):
			try:
				data += self.connection.recv(1024)
			except socket.error as err:
				raise ClientError('error read data', err)

		data_decoded = data.decode()

		status, info = data_decoded.split('\n', 1)
		info = info.strip()

		if status == 'error':
			raise ClientError(info)

		return info

	def put(self, key, value, timestamp=None):  # для сохранения метрик на сервере

		method = 'put'
		timestamp = timestamp or int(time.time())

		try:
			self.connection.sendall(
				f'{method} {key} {value} {timestamp}\n'.encode()
			)
		except socket.error as err:
			raise ClientError('error send data', err)

		self.read_data()  # смотрим ответ

	def get(self, key):  # для получения метрик

		method = 'get'

		try:
			self.connection.sendall(
				f'{method} {key}\n'.encode()
			)
		except socket.error as err:
			raise ClientError('error send data', err)

		payload = self.read_data()

		database = {}
		if payload == '':
			return database

		for row in payload.split('\n'):
			key, value, timestamp = row.split()
			if key not in database:
				database[key] = []
			database[key].append((int(timestamp), float(value)))

		return database


class ClientError(Exception):
	pass

