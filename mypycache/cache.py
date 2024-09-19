from backends.base import CacheBackend

class Cache:
	def __init__(self, backend: CacheBackend) -> None:
		self.backend = backend

	def set(self, key, value, ttl=None):
		self.backend.set(key, value)

	def get(self, key):
		return self.backend.get(key)

	def invalidate(self, key):
		pass

	def clear(self):
		pass 