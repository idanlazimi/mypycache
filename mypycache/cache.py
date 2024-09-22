from backends.base import CacheBackend

class Cache:
	def __init__(self, backend: CacheBackend) -> None:
		self.backend = backend

	def set(self, key, value, ttl=None):
		self.backend.set(key, value, ttl)

	def get(self, key):
		return self.backend.get(key)

	def invalidate(self, key):
		self.backend.invalidate(key)

	def clear(self):
		self.backend.clear()

	def	__len__(self):
		return len(self.backend) 