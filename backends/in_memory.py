from backends.base import CacheBackend
import time

class InMemoryBackend(CacheBackend):
	def __init__(self) -> None:
		self.store = {}
		self.expirations = {}

	def get(self, key):
		if key in self.expirations and time.time() > self.expirations[key]:
			self.invalidate(key)
		return self.store.get(key, None)

	def set(self, key, value, ttl=None):
		self.store[key] = value
		if ttl:
			self.expirations[key] = time.time() + ttl

	def invalidate(self, key):
		if key in self.store:
			del self.store[key]
		if key in self.expirations: 
			del self.expirations[key]
	
	def	clear(self):
		self.store.clear()
		self.expirations.clear()
	
	def __len__(self):
		return len(self.store)