from backends.base import CacheBackend

class InMemoryBackend(CacheBackend):
	def __init__(self) -> None:
		self.store = {}
		self.expirations = {}

	def get(self, key):
		return self.store.get(key, ValueError("Key does not exist"))

	def set(self, key, value, ttl=None):
		self.store[key] = value
		if ttl:
			pass

	def invalidate(self, key):
		pass
	def	clear(self):
		pass