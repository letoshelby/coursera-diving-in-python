from json import dumps
from functools import wraps


def to_json(func):
	@wraps(func)
	def wrapped(*args, **kw):
		result = dumps(func(*args, **kw))
		return result
	return wrapped


@to_json
def get_data():
	return {
		'data': 42
	}


