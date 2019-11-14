import os
import tempfile
import argparse
import json

STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
	if not os.path.exists(STORAGE_PATH):
		return {}

	with open(STORAGE_PATH, 'r') as file:
		raw_data = file.read()
		if raw_data:
			return json.loads(raw_data)

		return {}


def put(key, value):
	data = get_data()

	if key in data:
		data[key].append(value)
	else:
		data[key] = [value]

	with open(STORAGE_PATH, 'w') as f:
		f.write(json.dumps(data))


def get(keys):
	data = get_data()
	return data.get(keys)


parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value')

my_namespace = parser.parse_args()

if my_namespace.key and my_namespace.value:
	put(my_namespace.key, my_namespace.value)
elif my_namespace.key:
	print(get(my_namespace.key))
else:
	print(None)
