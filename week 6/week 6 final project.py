import asyncio

database = {}


class ClientServerProtocol(asyncio.Protocol):
	def connection_made(self, transport):
		self.transport = transport

	def data_received(self, data):
		self.transport.write(self.data_process(data.decode('utf-8').strip('\r\n')).encode('utf-8'))
		chunks = data.decode('utf-8').strip('\r\n').split(' ')
		cmd = chunks[0]

	def data_process(self, command):
		chunks = command.split(' ')
		if chunks[0] == 'get':
			return self.data_get(chunks[1])
		elif chunks[0] == 'put':
			return self.data_put(chunks[1], chunks[2], chunks[3])
		else:
			return 'error\n\n'

	def data_get(self, key):

		res = 'ok\n'
		if key == '*':
			for key, values in database.items():
				for value in values:
					res = res + key + ' ' + str(value[1]) + ' ' + str(value[0]) + '\n'
		else:
			if key in database.keys():
				for value in database[key]:
					res = res + key + ' ' + str(value[1]) + ' ' + str(value[0]) + '\n'

		return res + '\n'

	def data_put(self, key, value, timestamp):

		if key == '*':
			return 'error\nkey err\n\n'
		if key not in database.keys():
			database[key] = []
		database[key].append((int(timestamp), float(value)))

		return 'ok\n\n'


def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(ClientServerProtocol, host, port)
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()


